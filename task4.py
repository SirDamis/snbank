from random import randint
import time, json
from pathlib import Path

#Check account
def check_account(username):
    response = int(input('Enter account no: ')) #input account number
    with open('customer.txt', 'r') as file:#Open customer file
        customer_data = json.load(file) #Load file as json
    success = False
    for data in customer_data:#Loop trthrouh customer data
        if response == data['account_number']: #If account number is found
            success = True #Set succes to True if account number in customer data
            #Display customer data
            print("Account Details: ")
            print(f"Account Name: {data['account_name']}\nAccount Balance: {data['account_balance']}")
            print(f"Account Type: {data['account_type']}\nAccount Email: {data['account_email']}")
            print(f"Account Number: {data['account_number']}")
        if not success:  #If account number not found in customer data.
            print('Account number does not exists.')
    internal(username) #Call the internal function(which contains logout command)

#Function to create account.
def create_account(username):
    #input details
    account_name = input('Enter account name: ')
    account_balance = input('Enter opening account balance: ')
    account_type = input('Enter account type: ')
    account_email = input('Enter account email: ')
    account_number = int(randint(10**9,(10**10)-1))#Generate random number.

    #Save data to customer.txt file
    with open('customer.txt', 'r+') as file:#Open customer file
        try:
            customer_data = json.load(file) #load file as json
        except:
            customer_data = [] #Create empty list, if unable to load
        #Save data(dictionary) into the customer data (list)
        customer_data.append({
            'account_name': account_name,
            'account_balance' : account_balance,
            'account_type' : account_type,
            'account_email': account_email,
            'account_number': account_number
        })
        json.dump(customer_data, file) #Save data into the file

        #Print details
        print("Account successfully created.  Details: ")
        print(f"Account Name: {account_name}\nAccount Balance: {account_balance}")
        print(f"Account Type: {account_type}\nAccount Email: {account_email}")
        print(f"Account Number: {account_number}")

    internal(username)#Call the internal function
def internal(username):
    response = int(input('Enter:\n\t1 - To Create New Account.\n\t2 - To Check Account Details \n\t3 - To Logout\n'))
    if response == 1:
        create_account(username) #Call create account function
    elif response == 2:
        check_account(username) #Call check account function
    elif response == 3:
        with open('session.txt', 'a') as f: #Update user sesson file
            f.write(f'Staff with id : {username }, logout at {time.ctime()} .\n') #Add staff's details and loout time
        #Delete session file
        file_path = Path.cwd()/'session.txt' #Get session file path
        file_path.unlink() #Delete file from directory
        print('Logout Successful')
        main()
def login():
    username = input('Enter username: ') #enter username
    password = input('Enter password: ') #enter password
    with open('staff.txt') as file: #open staff file
        staffs_detail = json.load(file) #load file as json
    logged_in = None #set logged to None
    for value in staffs_detail: #Loops through staff data
        if username in value['Username'] and password == value['Password']: #perform authentication
            logged_in = True #Set loggerd in to true if authentication is succesful
            with open('session.txt', 'w') as f: #Create user sesson file
                f.write(f'Staff with id : {username }, logged in at {time.ctime()} .\n') #Write into user ssession.
            internal(username)#Call the core function which contains create, check function
    if not logged_in: #if staff detail not found
        print('No details found. Try again ')
        main()
def main():
    try:
        response = int(input('BANKING SYSTEM USING FILESYTEM.\n\tEnter 1 for Staff Login\n\tEnter 2 to Terminate\n'))
        if response == 1:
            login() #Call the login function if response is 1
        elif response == 2:
            print('Program Terminated')
            exit() #Quit the program if response is 2
        else:
            print('Incorrect input.')
            main() #Display the prompt if response is not 1 or 2
    except ValueError: #Prevent valueerror.
        main() 
main()
