""" 
This capstone project is to design program for small business which can be used to manage 
tasks assigned to each member of the team    
"""

# =====importing libraries===========
# Import datetime library which is used later on to find out the current date 
from datetime import date

# ====Login Section====
'''
below code which will allow the user to login 
    - read usernames and password from the user.txt file and store it in dictionary called user_dict
    - while loop to validate your user name and password.
'''
user_dict = {}
# read the user.txt file and extract the username and password 
with open('user.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split(", ")
        user_dict.update({line[0]: line[1]})

while True:
    # Ask username and password from the user
    user_name = input("Please enter username : ")

    """
    check if username entered by user is found in the data of users obtained from the user.txt file , 
    if its valid then progress further, else give error message that user name not found 
    and continue until the user has entered the correct user name
    """

    if user_name in user_dict:
        # ask user to enter the password for the user name which is valid 
        password = input("Please enter password : ")
        # check if the password entered by user matches the password obtained from user.txt file 
        if password == user_dict[user_name]:
            # password matched for the username
            print("Uesrname and password match ")
            break
        else:
            # print error message ,if password not matched 
            print("username found but password doesnt match, please try again ")

    else:
        # print username not found 
        print("Entered username not found , please try again")

"""
presenting the menu to the user, once the login is successful and making sure that the user input is 
coneverted to lower case.
"""

while True:

    menu = input('''Select one of the following Options below:
r  - Registering a user
a  - Adding a task
va - View all tasks
vm - view my task
e  - Exit
: ''').lower()

    '''
    Registration a new user, i.e  a new user is added to the user.txt file
            - Request user  of a new username
            - Request user  of a new password
            - Request user for  password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add new username and password to the user.txt file,
            - else eror message is presented that confirm password doesnt match to new password.
    '''
    if menu == 'r':
        # check to ensure that username 'admin' is permitted to perform registration process 
        if user_name == 'admin':

            """if username is admin , then present the new menu:
                 -presenting the menu for admin user : register new user /password or display stats 
                 -making sure that the user input is coneverted to lower case.
            """
            admin_menu = input('''Select one of the following Options below:
r  - Registering a user
ds - Display statistics 
e  - Exit
: ''').lower()

            # register new user and password to user.txt file 
            if admin_menu == 'r':
                new_username = input("Please enter new username to be registered : ")
                new_password = input("Please enter new password to be registered : ")
                while True:
                    confirm_password = input("Please enter password again to cnfirm : ")
                    # check if new password matches the confirmed password 
                    if new_password == confirm_password:
                        break
                    else:
                        # password and confirm password doesnt match , user asked to enter again
                        print("password and confirm password dont match ! Please enter confirm password again")
                # write the new user name and password to user.txt file 
                with open('user.txt', 'a') as f:
                    f.write(f"\n{new_username}, {new_password}")

            # Display statistics of total number of task and users 
            elif admin_menu == 'ds':
                task_count = 0
                user_count = 0

                with open("tasks.txt", "r") as f:
                    for line in f:
                        task_count += 1
                print("_" * 50)
                print(f"\nTotal number of tasks: {task_count}")

                with open("user.txt", "r") as f:
                    for line in f:
                        user_count += 1
                print(f"Total number of users: {user_count}")
                print("_" * 50)
        else:
            # user not permitted with admin acess 
            print("Not authorized with admin access, login required with admin credential")

        '''
        Allow a user to add a new task to task.txt file
            - Prompt a user for the following: 
                    - A username of the person whom the task is assigned to,
                    - A title of a task,
                    - A description of the task and 
                    - the due date of the task.
                - Get the current date.
                - Add the data to the file task.txt and
                - Completion status of task is defaulted to 'No'
        '''

    elif menu == 'a':
        # Ask user to enter below information for the new task 
        add_username = input("Please enter username of the person the task is assigned to : ")
        add_tile = input("Please enter the title of the task: ")
        add_description = input("Please enter description of the task: ")
        current_date = date.today()
        current_date = current_date.strftime("%d %b %Y")
        add_due_date = input("Please enter the due date in format; dd mmm yyyy: ")
        add_completed = 'No'
        # Write the data of new task to tasks.txt file 
        with open('tasks.txt', 'a') as f:
            f.write(f"\n{add_username}, {add_tile}, {add_description}, {current_date}, {add_due_date}, {add_completed}")

        '''
        The program will read the task from task.txt file and displaye all tasks to console in the 
        format of Output 2 in the task PDF(i.e. include spacing and labelling)
                - Read a line from the file.
                - Split that line where there is comma and space.
                - Then print the results in the format shown in the Output 2 
        '''
    elif menu == 'va':
        with open('tasks.txt', 'r') as f:
            for line in f:
                line = line.strip()
                line = line.split(", ")
                print("_" * 50)
                print(f"Task:\t\t\t{line[1]}")
                print(f"Assigned to:\t\t{line[0]}")
                print(f"Date assigned:\t\t{line[3]}")
                print(f"Due date:\t\t{line[4]}")
                print(f"Task complete?\t\t{line[5]}")
                print(f"Task description:\n{line[2]}")
        print("_" * 50)

        '''
        Read the task from task.txt file and display to the console task assigned to the logged in 
        user in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
                - Read a line from the file
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same as the username you have
                  read from the file.
                - If they are the same print it in the format of Output 2 in the task PDF
        '''
    elif menu == 'vm':
        pass
        with open('tasks.txt', 'r') as f:
            for line in f:
                line = line.strip()
                line = line.split(", ")
                if user_name == line[0]:
                    print("_" * 50)
                    print(f"Task:\t\t\t{line[1]}")
                    print(f"Assigned to:\t\t{line[0]}")
                    print(f"Date assigned:\t\t{line[3]}")
                    print(f"Due date:\t\t{line[4]}")
                    print(f"Task complete?\t\t{line[5]}")
                    print(f"Task description:\n{line[2]}")
            print("_" * 50)

        '''
        Option to exit the program 
        '''
    elif menu == 'e':
        print('Goodbye!!!')
        break

    else:
        # Message to user that valid option has not been choosen 
        print("You have made a wrong choice, Please Try again")
