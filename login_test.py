import unittest
import pyperclip
from user import Login
class TestLogin(unittest.TestCase):
    '''
    Test class that defines test cases for the login class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Login("Sally","Wanjiru","0711223344","sallyshick@gmail.com","1234")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Login.login_list = []
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Sally")
        self.assertEqual(self.new_user.last_name,"Wanjiru")
        self.assertEqual(self.new_user.phone_number,"0711223344")
        self.assertEqual(self.new_user.email,"sallyshick@gmail.com")
        self.assertEqual(self.new_user.password,"1234")
    def test_save_login(self):
        '''
        test_save_login test case to test if the login object is saved into
         the login list
        '''
        self.new_user.save_login()
        self.assertEqual(len(Login.login_list),1)
    def test_save_multiple_login(self):
        '''
        test_save_multiple_login to check if we can save multiple login
        objects to our login_list
        '''
        self.new_user.save_login()
        test_login = Login("Test","user","0711223344","test@user.com","password")
        test_login.save_login()
        self.assertEqual(len(Login.login_list),2)
    def test_delete_login(self):
        '''
        test_delete_login to test if we can remove a login from our login list
        '''
        self.new_user.save_login()
        test_login = Login("Test","user","0711223344","test@user.com","password")
        test_login.save_login()

        self.new_user.delete_login()
        self.assertEqual(len(Login.login_list),1)
    def test_find_login_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''
        self.new_user.save_login()
        test_login=Login("Test","User","07111223344","test@user.com","password")
        test_login.save_login()
        found_login=Login.find_by_number("07111223344")
        self.assertEqual(found_login.email,test_login.email)
    def test_login_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_login()
        test_login = Login("Test","user","0711223344","test@user.com","password")
        test_login.save_login()

        login_exists = Login.login_exist("0711223344")

        self.assertTrue(login_exists)
    def test_display_all_logins(self):
        '''
        method that returns a list of all login saved
        '''

        self.assertEqual(Login.display_login(),Login.login_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found login
        '''

        self.new_user.save_login()
        Login.copy_email("0711223344")

        self.assertEqual(self.new_user.email,pyperclip.paste())
if __name__ == '__main__':
    unittest.main()
