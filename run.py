#!/usr/bin/env python3.6
import pyperclip
class Login:
    """
    Class that generates new instances of login
    """
    login_list =[]
    def __init__(self,first_name,last_name,phone_number,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password=password
    def save_login(self):
        '''
        save_login method saves user objects into login_list
        '''
        Login.login_list.append(self)
    def delete_login(self):
        '''
        delete_login method deletes a saved login from the login_list
        '''
        Login.login_list.remove(self)
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a login that matches that number.

        Args:
        number: Phone number to search for
        Returns :
        Login of person that matches the number.
        '''

        for login in cls.login_list:
            if login.phone_number == number:
                return login
    @classmethod
    def login_exist(cls,number):
        '''
        Method that checks if a login exists from the login list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for login in cls.login_list:
            if login.phone_number == number:
                    return True

        return False
    @classmethod
    def copy_credentials(cls,number):
        login_found=Login.find_by_number(number)
        pyperclip.copy(login_found.credentials)
        '''
        method that returns the login_list
        '''
        return cls.login_list
    def display_login():
        '''
        Function that returns all the saved login
        '''
        return Login.login_list
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
    def find_login(number):
        '''
        Function that finds a login by number and returns the login
        '''
        return Login.find_by_number(number)
    def check_existing_login(number):
        '''
        Function that check if a contact exists with that number and return a Boolean
        '''
        return Login.login_exist(number)

    def display_login():
        '''
        Function that returns all the saved login
        '''
        return Login.display_login()
    def main():
        print("Hello welcome to twitter.")
        user_name=input()
        print(f"Hello{user_name}.Login")
        print('\n')
        while True:
            print("Use these short codes:ca -create new account,da -display accounts,fa -find an account,pa -password,ex -exit the account")
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
                save_login(create_login(f_name,l_name,p_number,e_address,password))
                print('\n')
                print(f"New User{f_name}{l_name}created")
                print('\n')
            elif short_code== 'da':
                if display_accounts():
                    print("Twitter,Facebook,Instagram")
                    print('\n')
                    for account in display_accounts:
                        print(f"{user.first_name}{user.last_name}.....{user.phone_number}")
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
                print("Enter the password")
                search_password=input()
                if check_existing_user(search_password):
                    search_user=find_user(search_password)
                    print(f"{search_user.first_name}")
                    print('-'*8)
                    print(f"Phone number.....{serch_user.phone_number}")
                    print(f"Email address....{search_user.email}")
                else:
                    print("That password does not exist")

            elif short_code == "ex":
                print("Bye .......")
                break
            else:
                print("I really didn't get that. Please use the short codes")
if __name__=='__main__':
    main()
