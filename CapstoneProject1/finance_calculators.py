# Financial calculator which provides user to acess two financial calculator 
# 1. Investment calculator 
# 2. Home loan repayment calculator 

import math

# Ask user which calculator they would like to use 

calc_option = input("""
Choose either 'investment' or 'bond' from the menu below to proceed :
investment -  to calculate the amount of interest you will earn on your investment
bond       -  to calculate the amount you will have to pay on a home loan 
""")

# convert option to lower case 
calc_option = calc_option.lower()

if calc_option == "investment":
    amount = round(float(input("Please enter deposit amount : ")), 2)
    int_rt = int(input("Please enter the interest rate as number only : "))
    year = int(input("Please enter the number of years for investment : "))
    interest = input("Please enter if you wish to have 'simple' or 'compound' interest type : ")
    p = amount
    r = int_rt / 100
    t = year

    if interest == "simple":
        # calculate simple interest 
        A = round(p * (1 + r * t), 2)
        print(f"amount you will get back after {t} yrs of inveestment of principal amount {p} using SI : {A}")
    elif interest == "compound":
        # calculate compound interest 
        A = round(p * math.pow((1 + r), t), 2)
        print(f"amount you will get back after {t} yrs of inveestment of principal amount {p} using CI : {A}")
    else:
        pirnt("invalid option entered ")

elif calc_option == "bond":
    loan = round(float(input("Please enter present house value : ")), 2)
    int_rt = int(input("Please enter the interest rate as number only : "))
    month = int(input("Please enter the number of months for repayment term : "))
    p = loan
    r = int_rt / (12 * 100)
    n = month
    x = round((p * r) / (1 - math.pow((1 + r), -n)))
    print(f"amount you will repay each month  : {x}")

else:
    print("Invalid option entered for financial calculator")