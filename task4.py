from random import randint
import time, json
from pathlib import Path

def check_account(username):
    response = int(input('Enter account no: '))
    with open('customer.txt', 'r') as file:
        customer_data = json.load(file)
    success = False
    for data in customer_data:
        if response == data['account_number']:
            success = True
            print("Account Details: ")
            print(f"Account Name: {data['account_name']}\n\tBalance: {data['account_balance']}")
            print(f"Account Type: {data['account_type']}\n\tAccount Email: {data['account_email']}")
            print(f"Account Number: {data['account_number']}")
        if not success:  
            print('Account number does not exists.')
    internal(username)
def create_account(username):
    account_name = input('Enter account name: ')
    account_balance = input('Enter opening account balance: ')
    account_type = input('Enter account type: ')
    account_email = input('Enter account email: ')
    account_number = int(randint(10**9,(10**10)-1))

    #Save data to customer.txt file
    with open('customer.txt', 'r+') as file:
        try:
            customer_data = json.load(file)
        except:
            customer_data = []
        customer_data.append({
            'account_name': account_name,
            'account_balance' : account_balance,
            'account_type' : account_type,
            'account_email': account_email,
            'account_number': account_number
        })
        json.dump(customer_data, file)

        print("Account successfully created.  Details: ")
        print(f"Account Name: {account_name}\n\tBalance: {account_balance}\n")
        print(f"Account Type: {account_type}\n\tAccount Email: {account_email}")
        print(f"Account Number: {account_number}")

    internal(username)
def internal(username):
    response = int(input('Enter:\n\t1 To Create New Account.\n\t2 To Check Account Details \n\t3 To Logout\n'))
    if response == 1:
        create_account(username)
    elif response == 2:
        check_account(username)
    elif response == 3:
        with open('session.txt', 'a') as f: #Update user sesson file
            f.write(f'Staff with id : {username }, logout at {time.ctime()} .\n')
        #Delete session file
        file_path = Path.cwd()/'session.txt'
        file_path.unlink()
        print('Logout Successful')
        main()
def login():
    username = input('Enter username: ')
    password = input('Enter password: ')
    with open('staff.txt') as file:
        staffs_detail = json.load(file)
    logged_in = None
    for value in staffs_detail:
        if username in value['Username'] and password == value['Password']:
            logged_in = True
            with open('session.txt', 'w') as f: #Create user sesson file
                f.write(f'Staff with id : {username }, logged in at {time.ctime()} .\n')
            internal(username)
    if not logged_in:
        print('No details found. Try again ')
        main()
def main():
    try:
        response = int(input('BANKING SYSTEM USING FILESYTEM.\n\tEnter 1 for Staff Login\n\tEnter 2 to Terminate\n'))
        if response == 1:
            login()
        elif response == 2:
            print('Program Terminated')
            exit()
        else:
            print('Incorrect input.')
            main()
    except ValueError:
        main()     
main()
