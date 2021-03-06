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
        for login in Login.login_list:
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

    def add_user(self):
        Login.login_list.append(self)

class AddUser():
    user_list=[]
    def __init__(self,username,password):
        self.username = username
        self.password =password

    def add_user(self):
        AddUser.user_list.append(self)
# if __name__=='__main__':
#     main()
