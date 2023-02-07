# ------------------------------------------------------------------------------
#  inventory.py
#
# Description:  A stock-taking and inventory management program for Nike
#               warehouses that reads inventory input file and allows the
#               user to perform a range of functions.These functions include
#               capture shoe information from user and add the same to list
#               view all the shoe information and view in tabular format
#               determining the product with the lowest stock and option for
#               restocking based on user choice
#               searching for a shoe by product code
#               determining the product with the highest quantity
#               value per item : calculating the value of each item entry
# -------------------------------------------------------------------------------

# impor python library required as part of project
from tabulate import tabulate
import pandas as pd


# ========The beginning of the class==========
# Shoe class with attribute : country, code, product, cost, quantity
# initialize each attribute and
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        #       return the cost of the shoe
        return int(self.cost)

    def get_quantity(self):
        #       return the quantity of the shoes.
        return int(self.quantity)

    def get_code(self):
        #       return the product code
        return self.code

    def set_quantity(self, quantity):
        #       set the quantity of the shoes.
        self.quantity = int(quantity)

    def __str__(self):
        #       returns a string representation of a class.
        return f"""
Country:  {self.country}
Code:     {self.code}
Product:  {self.product}
Cost:     {self.cost}
Quantity: {self.quantity}
"""


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    """
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    """
    try:
        with open('inventory.txt', 'r') as f:
            next(f)
            for line in f:
                line = line.strip()
                line = line.split(",")
                try:
                    shoe_list.append(Shoe(line[0], line[1], line[2], line[3], line[4]))
                except IndexError:
                    # Index error in the list of data
                    print("Some Item in \"inventory.txt\" is not \
formatted correctly.Correct formatted data should follow : \
\"country,code,product,cost,quantity\" with no empty lines \
between products.")
    # If the file cannot be found, give an error message and exit the program
    except FileNotFoundError:
        print("Inventory.txt file cannot be found. Please ensure that the file exist.")


def capture_shoes():
    """
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    """

    country = input("Please enter the country for the product : ")
    code = input("Please enter the code of the product: ").upper()
    product = input("Please enter the name of the product: ")
    while True:
        try:
            cost = int(input("Please enter the cost of the product: "))
        except ValueError:
            print("Cost needs to be entered as integer only, try again")
        else:
            break

    while True:
        try:
            quantity = int(input("Please enter the quantity of this product: "))
        except ValueError:
            print("Quantity needs to be entered as integer only , try again")
        else:
            break

            # create the Shoe object using the information provided by the user
    shoe_obj = Shoe(country, code, product, cost, quantity)
    # Adds the new shoe to inventory.txt file
    with open("inventory.txt", "a", encoding="utf-8") as f:
        f.writelines(f"\n{country},{code},{product},{cost},{quantity}")
    # Adds the item to shoes list
    shoe_list.append(shoe_obj)
    print("Shoe details have been added. Returning to main menu.")


def view_all():
    """
    This function will iterate over the shoes list and
    print the details of the shoe in tabular format
    """
    df = pd.DataFrame(None)
    df = pd.DataFrame([s.__dict__ for s in shoe_list])
    print(tabulate(df, headers='keys', tablefmt='psql'))


def re_stock():
    """
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    """
    # find the shoe with lowest stock quantity
    min_shoe = min(shoe_list, key=lambda x: x.get_quantity())
    print(f"{min_shoe.get_code()} has the lowest quantity of stock")
    # Ask user if restocking needs to be performed
    re_stock_check = input("Please advise if you would like to restock (y/n): ").lower()
    # Restocking to be performed
    if re_stock_check == 'y':
        while True:
            try:
                new_stock = int(input("Please enter the new quantity of stock required : "))
                with open('inventory.txt', 'w') as f:
                    print("Country,Code,Product,Cost,Quantity", file=f)
                    for shoe in shoe_list:
                        if shoe.get_code() == min_shoe.get_code():
                            shoe.set_quantity(new_stock)
                            print(*vars(shoe).values(), sep=',', file=f)
                        else:
                            print(*vars(shoe).values(), sep=',', file=f)
                print(f"{min_shoe.get_code()} has beens successfully restocked. New stock is {new_stock}.")
            except ValueError:
                print("You can only enter an integer. Please try again.")
            else:
                break
    # if invalid option or user doesnt want to restock then return back to main menu
    elif re_stock_check == "n":
        print("Restock selection not opted , Returning to menu...")
    else:
        print("Invalid option selected for restocking. Please try again.")


def search_shoe():
    """
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    """
    shoe_search = ""
    found_search_shoe = None
    shoe_search = input("Please enter the product code of the shoe : ").upper()
    for shoe in shoe_list:
        if shoe.get_code() == shoe_search:
            found_search_shoe = shoe
    if found_search_shoe is None:
        print(f"Sorry, a shoe with the product code {shoe_search} could \
not be found. Please try again.")
    else:
        print(f"Shoe found with code: {shoe_search} \n {found_search_shoe}")


def value_per_item():
    """
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    """
    for shoe in shoe_list:
        cost_shoe = shoe.get_cost() * shoe.get_quantity()
        shoe.value_per_item = cost_shoe
    df = pd.DataFrame([s.__dict__ for s in shoe_list])
    print(tabulate(df, headers='keys', tablefmt='psql'))


def highest_qty():
    """
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    """
    max_shoe = max(shoe_list, key=lambda x: x.get_quantity())
    print(f" Shoe on Sale !!! \n {max_shoe}")


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
choice = ""
read_shoes_data()
# Displays a menu until the user enters quit
while choice != "q":

    # Prints a list of options for the menu
    choice = input(""" Please choose from below option: 
c  - capture data for shoe 
v  - View data about shoe
rs - Restock the lowest quantity of shoe 
s  - Search for a shoe by product code
vpi- value per item (cost*quantity) for each shoe
h -  highest quantity - On Sale 
q -   Quit the program
""").lower()

    # If user enters c, allows user to add a new shoe to the inventory
    if choice == "c":
        capture_shoes()
    # If user enters v, prints information about all shoes
    elif choice == "v":
        view_all()
    # If user enters rs, restocks the lowest quantity shoe
    elif choice == "rs":
        re_stock()
    # If user enters s, allows user to search for a shoe by product code
    elif choice == "s":
        search_shoe()
    # If user enters vps, prints table of shoes information with
    # additional column for the value per shoe (cost*quantity)
    elif choice == "vpi":
        value_per_item()
    # If user enters h, prints a sale notice for the shoe with the highest
    # quantity
    elif choice == "h":
        highest_qty()
    # If the user enters q, quits the program
    elif choice == "q":
        print("Thank you for using the Nike Warehouse system. Goodbye!")
        break
    else:
        # If the option the user entered was not recognised, prints an
        # error message and allows them to try again
        print(f"The option \"{choice}\" entered is not recognised, please try again.")
        continue