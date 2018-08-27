#!/usr/bin/env python3.6

from run import Login, AddUser
def create_login(fname,lname,phone,email,password):
    '''
    Function to create a new login
    '''
    new_login = Login(fname,lname,phone,email,password)
    return new_login
def save_login(login):
    '''
    Function to save login
    '''
    login.save_login()
def del_login(login):
    '''
    Function to delete login
    '''
    login.delete_contact()
def find_user(number):
    '''
    Function that finds a login by number and returns the login
    '''
    return Login.find_by_number(number)
def check_existing_user(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Login.login_exist(number)

def display_accounts():
    '''
    Function that returns all the saved login
    '''
    return Login.display_login()
def main():
    print("Hello welcome.")
    user_name=input()
    print(f"Hello{user_name}.Login")
    print('\n')
    while True:
        print("Use these short codes:ca -create new account,da -display accounts,fa -find an account,pa -login,ex -exit the account")
        short_code=input().lower()
        if short_code=='ca':
            print("New Account")
            print("-"*10)
            print("First name .....")
            f_name=input()
            print("Last name....")
            l_name=input()
            print("Phone number....")
            p_number=input()
            print("Email address....")
            e_address=input()
            print("Password....")
            print("-"*8)
            password=input()
            save_login(create_login(f_name,l_name,p_number,e_address,password))
            print('\n')
            print(f"New User{f_name}{l_name}created")
            print('\n')
        elif short_code== 'da':
            if display_accounts():
                print("Twitter,Facebook,Instagram")
                print('\n')
                for account in Login.login_list:
                    print(f"{account.first_name}{account.last_name}.....{account.phone_number}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any account saved yet")
                print('\n')
        elif short_code=='fa':
            print("Enter the number you want to search for")
            search_number=input()
            if check_existing_user(search_number):
                search_user=find_user(search_number)
                print(f"{search_user.first_name}{search_user.last_name}")
                print('-' * 20)
                print(f"Phone number.......{search_user.phone_number}")
                print(f"Email address.......{search_user.email}")
            else:
                print("That contact does not exist")
        elif short_code=='pa':
            print("Enter the login")
            search_login=input()
            if check_existing_user(search_login):
                search_user=find_user(search_login)
                print(f"{search_user.first_name}")
                print(f"Phone number.....{serch_user.phone_number}")
                print(f"Email address....{search_user.email}")
            else:
                print("That login does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")
if __name__=='__main__':
    main()
