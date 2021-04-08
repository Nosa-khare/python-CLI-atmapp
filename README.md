# atmApp

Replica/Immitation  of Banking system

## Code Setup
* Install python 3 on system
* Clone repository
* run code using an IDE (e.g Pycharm, VS code, etc). Code can also be run on the terminal

## Code features

The code consists of ten functions:

* _startPage:_ 
    
    After the prgram introduces the user to the bank, this presents the user with options to either login, open a new accout with the bank, or close the program.


* _register:_
  
    Here the customer details are collected, account name, account email, account password, account type, opening balance, etc.
    The generateAccounNumber function is called to provide a new account number for user. 
    After successful account creation, the details of the new account is stored in a dictionary and kept in the customer database.


* _generateAccountNumber_:
  
    when called this helps generate a 10 digit random accout number starting with 150..


* _login:_
  
    This function collects the customer details and compares with the details in customerDatabase.txt to verify for successful login.
    After a successful login, program proceeds to transactions page


* _getPassword:_
  
    This is called in the login function after collecting user password. It checkes through customerDatabase to verify password


* _transactions:_

    This function asks the user the purpose for logging in, i.e if to make a withdrawal, a deposit or to register a complaint.
    when the choice is entered, the corresponding funtion is called.


* _deposit:_
  
    This enables the user make cash deposit into his/her account. After deposit is made the account balance is updated.


* _withdrawal:_
  
    This enables the user make cash withdrawal from his/her account. After withdrawal is made the account balance is updated.


* _complaints:_
  
    Here the user inputs what ever complaints he/she has. the complaints are then stored in a dictionary and entered into the complaint database.


* _endPage:_
  
    This brings up the exit options.
