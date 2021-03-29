import textwrap as tw
from datetime import datetime

time_date = datetime.now()

username_data = ['Admin']
password_data = ['01234567']

account_details = {'Admin': 500.00}  # dict containing the account balance of all users.

complaint_log = {}  # dict containing all complaints lodged by users


def endPage(username):
    """ last page of the app that leads to exit """

    while True:
        another_transaction = input(tw.dedent("""
                                Would you like to perform another transaction?
                                Enter yes or no
                                ---> """))

        if another_transaction.lower() == 'yes':
            transactions(username)
            break
        elif another_transaction.lower() == 'no':
            print('\nThank you for banking with us!')
            exit(0)
        else:
            print("\nInvalid response")


def complaints(username):
    """ function to handle collection of complaints from users """

    complaint_count = 0  # helps count number of complaint lodged by user for dict formatting

    complaint = input("\nWhat issue would you like to report?\n---> ")
    complaint_log[username + "_" + str(complaint_count)] = complaint  # collects the complaint and inputs it in the
    # complaint dict as 'username_count': 'complaint'.
    print("Complaint logged successfully\nThank you for contacting us!")
    complaint_count += 1  # increases the complaint count by one

    endPage(username)


def deposit(username):
    """ to collect deposit and add to account balance """

    while True:
        try:
            deposit_amount = int(input("\nHow much would you like to deposit?\n---> "))
            account_details[username] += deposit_amount  # increases account balance with deposit amount
            print(tw.dedent(f"""
                ${deposit_amount} deposited successfully!
                Current balance: ${account_details[username]}
                """))
            endPage(username)
        except ValueError:  # to handle non-numeric inputs
            print("Invalid input")
            endPage(username)


def withdrawal(username):
    """ function to dispense cash withdrawals """

    while True:
        try:
            withdrawal_amount = int(input("\nHow much would you like to withdraw?\n---> "))
            if int(withdrawal_amount) <= account_details[username] - 1:  # check if account balance is sufficient to
                # dispense withdrawal amount (leaving at least $1 balance)
                input(f"${withdrawal_amount}\n"  # display amount dispensed by ATM
                      "Take your cash and press 'Enter'\n")
                account_details[username] -= withdrawal_amount  # decreases account balance with deposit amount

                endPage(username)
            else:
                print("Insufficient funds")
                endPage(username)
            break

        except ValueError:
            print("Invalid input")
            endPage(username)


def transactions(username):
    """ function to allow user select what
        transaction is to be performed """

    print(tw.dedent("""
                    What transaction would you like to perform?
                    1. Make a cash withdrawal
                    2. Make a cash deposit
                    3. Register a complaint\n"""))

    while True:  # repeat process of collecting input until valid

        selected_option = input("Enter 1, 2 or 3 \n---> ")
        print(selected_option)

        if selected_option == "1":
            withdrawal(username)
            break
        elif selected_option == "2":
            deposit(username)
            break
        elif selected_option == "3":
            complaints(username)
            break
        else:
            print("invalid option. Please try again\n")


def login():
    """ function to enable registered users login """

    while True:
        username = input("\nEnter your username\n---> ")

        if username in username_data:  # confirm username exists in database
            break
        else:
            print("Username entered does not exist. Try again\n")

    while True:
        password = input("Enter your password\n---> ")
        if (password in password_data and
                username_data.index(username) == password_data.index(password)):  # to check if password exists in
            # database and whether it matches the username entered

            print(
                f"\nWelcome {username}!\n"
                f"{time_date.strftime('%a, %b %d, 20%y')}\n"  # displays the current date.
                f"{time_date.strftime('%I:%M:%S %p')}"  # displays the current time.
            )

            transactions(username)
            break
        else:
            print("\nIncorrect password. Try again\n")


def register():

    """ function to enable new users register their account """

    username = input("\nEnter a username \n---> ")

    if username in username_data:
        print("Username has been taken.\n")
        register()
    else:
        username_data.append(username)

    while True:
        password = input("\nEnter a password\n"
                         "(password must be at least 8 characters)\n"
                         "---> ")

        if len(password) >= 8:
            password_data.append(password)
            print(tw.dedent("""
                            Registration successful.
                            Proceed to login.
                            """))
            account_details[username] = 100.00  # registers new accounts with a balance of $100
            login()
            break
        else:
            print("\nPassword too weak!")


def startPage():

    """ start of application"""

    print(tw.dedent("""
                    Welcome to myATM!
                    1. Login
                    2. Open Account\n"""))

    while True:  # repeat process of collecting input until valid

        selected_option = input("Enter 1 or 2 \n---> ")
        print(selected_option)

        if selected_option == "1":
            login()
            break
        elif selected_option == "2":
            register()
            break
        else:
            print("invalid option. Please try again\n")


# On app launch
startPage()
