import unittest
from run import Login
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

if __name__ == '__main__':
    unittest.main()
