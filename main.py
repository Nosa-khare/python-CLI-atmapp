import textwrap as tw
from datetime import datetime
from random import randint

import json

time_date = datetime.now()


def endPage(details):

    """ last page of the app that leads to exit """

    while True:
        another_transaction = input(tw.dedent("""
                                Would you like to perform another transaction?
                                Enter yes or no
                                ---> """))

        if another_transaction.lower() == 'yes':
            transactions(details)
            break
        elif another_transaction.lower() == 'no':
            print(f"\nThank you for banking with us {details['Account Name']}!")
            exit()
        else:
            print("\nInvalid response")


def complaints(details):
    """ function to handle collection of complaints from users """

    complaint_count = 1  # helps count number of complaint lodged by user for dict formatting

    complaint = input("\nWhat issue would you like to report?\n---> ")

    complaint_log_dict = {details['Account Name'] + "_" + str(  # dict containing all complaints lodged by users
        complaint_count): complaint}  # inputs it in the complaint dict as 'username_count': 'complaint'.

    with open('complaintLog.txt', 'a+') as complaintLog:
        complaintLog.write(json.dumps(complaint_log_dict))
        complaintLog.write("\n")

    print("\nComplaint logged successfully\nThank you for contacting us!")
    complaint_count += 1  # increases the complaint count by one
    endPage(details)


def deposit(details):
    """ to collect deposit and add to account balance """

    while True:
        try:
            deposit_amount = int(input("\nHow much would you like to deposit?\n---> "))
            details['Account Balance'] += deposit_amount  # increases account balance with deposit amount
            print(tw.dedent(f"""
                ${deposit_amount} deposited successfully!
                Current balance: ${details['Account Balance']}
                """))
            endPage(details)
        except ValueError:  # to handle non-numeric inputs
            print("Invalid input")
            endPage(details)


def withdrawal(details):
    """ function to dispense cash withdrawals """

    while True:
        try:
            withdrawal_amount = int(input("\nHow much would you like to withdraw?\n---> "))

            if int(withdrawal_amount) <= details['Account Balance'] - 1:  # check if account balance is sufficient to
                # dispense withdrawal amount (leaving at least $1 balance)

                input(f"${withdrawal_amount}\n"  # display amount dispensed by ATM
                      "Take your cash and press 'Enter'\n")
                details['Account Balance'] -= withdrawal_amount  # decreases account balance with deposit amount
                endPage(details)
            else:
                print("Insufficient funds")
                endPage(details)
            break

        except ValueError:
            print("Invalid input")
            endPage(details)


def transactions(details):
    """ function to allow user select what
        transaction is to be performed """

    print(tw.dedent("""
                    What transaction would you like to perform?
                    1. Make a cash withdrawal
                    2. Make a cash deposit
                    3. Register a complaint
                    4. Close App\n"""))

    while True:  # repeat process of collecting input until valid response is gotten

        selected_option = input("1, 2, 3, 4 \n---> ")
        print(selected_option)

        if selected_option == "1":
            withdrawal(details)
            break
        elif selected_option == "2":
            deposit(details)
            break
        elif selected_option == "3":
            complaints(details)
            break
        elif selected_option == "4":
            endPage(details)
        else:
            print("invalid option. Please try again\n")


def getPassword(details):
    password = input("Enter your password\n---> ")

    if password == details['Password']:  # to check if password is correct

        print(
            f"\nWelcome {details['Account Name']}!\n"
            f"{time_date.strftime('%a, %b %d, 20%y')}\n"  # displays the current date.
            f"{time_date.strftime('%I:%M:%S %p')}"  # displays the current time.
            )
        transactions(details)
    else:
        print("\nIncorrect password. Try again\n")
        getPassword(details)


def login():
    """ function to enable registered users login """

    account_login = input("\nEnter your account number\n---> ")

    customerDatabase_file = open("customerDatabase.txt", "r").read()
    customer_list = customerDatabase_file.splitlines()

    found_account = False
    count = 1
    for details in customer_list:
        details = json.loads(details)
        if account_login == details['Account Number']:  # confirm username exists in customerDatabase.txt
            getPassword(details)
            found_account = True
        if count == len(customer_list) and not found_account:  # if all dictionaries has been looped through
            # and not found
            print(f"No record of account with Account Number: {account_login} found")
            startPage()


def generateAccountNumber():
    # generating an account number
    number_list = [1, 5, 0]  # to enable every generated acc number start with 150
    [number_list.append(randint(0, 9)) for _ in range(7)]
    account_number = "".join([str(i) for i in number_list])  # converts all integers to strings and joins
    return account_number


def register():
    """ function to enable new users register their account """

    print("****** Register ******")

    firstname = input("\nEnter your Firstname \n---> ")
    lastname = input("\nEnter your Firstname \n---> ")

    account_name = firstname + ' ' + lastname  # to get an account name

    while True:
        account_email = input("\nEnter your you email address \n---> ")
        if "." in list(account_email) and "@" in list(account_email):
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
                        "Account Balance": opening_balance,
                        "Account Email": account_email,
                        "Password": account_password,
                        "Account Type": account_type
                        }

    # adding the dictionary of the new account created to the customer txt file
    customerDatabase = open("customerDatabase.txt", 'a')
    customerDatabase.write(json.dumps(customer_details))  # writes customer_details as a dict into customer file
    customerDatabase.write("\n")  # writes a newline in file in view of next dump
    customerDatabase.close()

    print("\nAccount has been registered successfully!\n"
          f"These are your account details: \n{customer_details}")
    endPage(firstname)


def startPage():
    """ start of application"""

    print(tw.dedent("""
                    1. Login
                    2. Open A New Account
                    3. Close App\n"""))

    selected_option = input("1, 2, 3 \n---> ")
    print(selected_option)

    if selected_option == "1":
        login()
    elif selected_option == "2":
        register()
    elif selected_option == "3":
        exit()
    else:
        print("invalid option. Please try again\n")
        startPage()  # repeat process of collecting input until valid response gotten from user


# Initialize app

print("Welcome to BankPHP!")

startPage()
