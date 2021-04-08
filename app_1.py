import textwrap as tw
from datetime import datetime
from random import randint

import json

time_date = datetime.now()

complaint_log = {}  # dict containing all complaints lodged by users


# def endPage(username):
#
#     """ last page of the app that leads to exit """
#
#     while True:
#         another_transaction = input(tw.dedent("""
#                                 Would you like to perform another transaction?
#                                 Enter yes or no
#                                 ---> """))
#
#         if another_transaction.lower() == 'yes':
#             transactions(username)
#             break
#         elif another_transaction.lower() == 'no':
#             print('\nThank you for banking with us!')
#             exit(0)
#         else:
#             print("\nInvalid response")
#
#
# def complaints(username):
#
#     """ function to handle collection of complaints from users """
#
#     complaint_count = 0  # helps count number of complaint lodged by user for dict formatting
#
#     complaint = input("\nWhat issue would you like to report?\n---> ")
#     complaint_log[username + "_" + str(complaint_count)] = complaint  # collects the complaint and inputs it in the
#     # complaint dict as 'username_count': 'complaint'.
#     print("Complaint logged successfully\nThank you for contacting us!")
#     complaint_count += 1  # increases the complaint count by one
#
#     endPage(username)
#
#
# def deposit(username):
#
#     """ to collect deposit and add to account balance """
#
#     while True:
#         try:
#             deposit_amount = int(input("\nHow much would you like to deposit?\n---> "))
#             account_details[username] += deposit_amount  # increases account balance with deposit amount
#             print(tw.dedent(f"""
#                 ${deposit_amount} deposited successfully!
#                 Current balance: ${account_details[username]}
#                 """))
#             endPage(username)
#         except ValueError:  # to handle non-numeric inputs
#             print("Invalid input")
#             endPage(username)
#
#
# def withdrawal(username):
#
#     """ function to dispense cash withdrawals """
#
#     while True:
#         try:
#             withdrawal_amount = int(input("\nHow much would you like to withdraw?\n---> "))
#             if int(withdrawal_amount) <= account_details[username] - 1:  # check if account balance is sufficient to
#                 # dispense withdrawal amount (leaving at least $1 balance)
#                 input(f"${withdrawal_amount}\n"  # display amount dispensed by ATM
#                       "Take your cash and press 'Enter'\n")
#                 account_details[username] -= withdrawal_amount  # decreases account balance with deposit amount
#
#                 endPage(username)
#             else:
#                 print("Insufficient funds")
#                 endPage(username)
#             break
#
#         except ValueError:
#             print("Invalid input")
#             endPage(username)
#
#
# def transactions(username):
#
#     """ function to allow user select what
#         transaction is to be performed """
#
#     print(tw.dedent("""
#                     What transaction would you like to perform?
#                     1. Make a cash withdrawal
#                     2. Make a cash deposit
#                     3. Register a complaint\n"""))
#
#     while True:  # repeat process of collecting input until valid
#
#         selected_option = input("Enter 1, 2 or 3 \n---> ")
#         print(selected_option)
#
#         if selected_option == "1":
#             withdrawal(username)
#             break
#         elif selected_option == "2":
#             deposit(username)
#             break
#         elif selected_option == "3":
#             complaints(username)
#             break
#         else:
#             print("invalid option. Please try again\n")
#
#
def login():

    """ function to enable registered users login """

    while True:
        account_login = input("\nEnter your username\n---> ")



        if username in username_data:  # confirm username exists in customerDatabase.txt
            break
        else:
            print("Username entered does not exist. Try again\n")

    while True:
        password = input("Enter your password\n---> ")
        if (password in password_data and
                username_data.index(username) == password_data.index(password)):  # to check if password exists in
            # customerDatabase.txt and whether it matches the username entered

            print(
                f"\nWelcome {username}!\n"
                f"{time_date.strftime('%a, %b %d, 20%y')}\n"  # displays the current date.
                f"{time_date.strftime('%I:%M:%S %p')}"  # displays the current time.
            )

            transactions(username)
            break
        else:
            print("\nIncorrect password. Try again\n")


def generateAccountNumber():
    # generating an account number
    number_list = [1, 5, 0]  # to enable every generated acc number start with 150
    [number_list.append(randint(0, 9)) for x in range(7)]
    account_number = "".join([str(i) for i in number_list])  # converts all integers to strings and joins
    return account_number


def register():
    """ function to enable new users register their account """

    print("****** Register ******")

    firstname = input("\nEnter your Firstname \n---> ")
    lastname = input("\nEnter your Firstname \n---> ")

    account_name = firstname, lastname   # to get an account name

    while True:
        account_email = input("\nEnter your you email address \n---> ")
        if "." in list(account_email):
            break
        else:
            print("Invalid email address")

    while True:
        account_password = input("\nEnter a password\n"
                                 "(password must be at least 8 characters)\n"
                                 "---> ")
        if len(account_password) >= 8:
            break
        else:
            print("\nPassword too weak!")

    accounts_dict = {
        "1": "Current Account",
        "2": "Savings account",
        "3": "Recurring Deposit Account",
        "4": "Fixed Deposit Account"
    }

    # to select an account type
    while True:
        account_type = input(tw.dedent("""
                                    Choose an account type
                                    1. Current Account
                                    2. Savings account
                                    3. Recurring Deposit Account
                                    4. Fixed Deposit Account
                                    (1, 2, 3, 4): """))
        if account_type in ["1", "2", "3", "4"]:
            account_type = accounts_dict.get(
                account_type)  # set account type to corresponding name from accounts dict
            break
        else:
            print("Invalid selection!")

    # deposit an opening balance
    while True:
        try:
            opening_balance = int(input("Enter Opening balance (In figures): "))
            break
        except ValueError:
            print("Invalid Amount!")

    account_number = generateAccountNumber()

    customer_details = {"Account Name": account_name,
                        "Account Number": account_number,
                        "Account Balance": f"${opening_balance}",
                        "Account Email": account_email,
                        "Password": account_password,
                        "Account Type": account_type
                        }

    # adding the dictionary of the new account created to the customer txt file
    customerDatabase = open("customerDatabase.txt", 'a')
    customerDatabase.write(json.dumps(customer_details))  # writes customer_details as a dict into customer file
    customerDatabase.write("\n")  # writes a newline in file in view of next dump
    customerDatabase.close()

    print("Account has been registered successfully!"
          f"This is your account details: {customer_details}")


def startPage():
    """ start of application"""

    print(tw.dedent("""
                    Welcome to BankPHP!
                    1. Login
                    2. Open A New Account
                    3. Close App\n"""))

    while True:  # repeat process of collecting input until valid

        selected_option = input("Enter 1 or 2 \n---> ")
        print(selected_option)

        if selected_option == "1":
            login()
            break
        elif selected_option == "2":
            register()
            break
        elif selected_option == "3":
            exit()
        else:
            print("invalid option. Please try again\n")


# Initialize app
startPage()
