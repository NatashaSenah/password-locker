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
