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


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Sally")
        self.assertEqual(self.new_user.last_name,"Wanjiru")
        self.assertEqual(self.new_user.phone_number,"0711223344")
        self.assertEqual(self.new_user.email,"sallyshick@gmail.com")
        self.assertEqual(self.new_user.password,"1234")


if __name__ == '__main__':
    unittest.main()
