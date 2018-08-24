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
