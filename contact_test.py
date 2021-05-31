import pyperclip
import unittest
from contact import Contact
class TestContacts(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("josephat","Otieno","0712345678","jose@gmail.com")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Contact.contact_list=[]

        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"josephat")
        self.assertEqual(self.new_contact.last_name,"Otieno")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"jose@gmail.com")

# if __name__ == '__main__':
#     unittest.main()
    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
         '''
        self.new_contact.save_contact() #saving the new contact
        self.assertEqual(len(Contact.contact_list),1) 

    def test_save_multiple_contacts(self):
        '''    
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_contact.save_contact()
        test_contact=Contact("Test","user","071793849","test@user.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_contact.save_contact()
        test_contact=Contact("Test","user","071793849","test@user.com")
        test_contact.save_contact()

        self.new_contact.delete_contact() #deleting a contact object
        self.assertEqual(len(Contact.contact_list),1)

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by number
        '''
        self.new_contact.save_contact()
        test_contact=Contact("Test","user","071793849","test@user.com")
        test_contact.save_contact()

        found_contact=Contact.find_contact_by_number("071793849")

        self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exist(self):
        '''
        test to check if we can return a boolean if we 
        cannot find a contact"
        '''
        self.new_contact.save_contact()
        test_contact=Contact("Test","user","071793849","test@user.com")
        test_contact.save_contact()

        contact_exist=Contact.contact_exist("071793849")

        self.assertTrue(contact_exist)

    def test_display_all_contacts(self):
        '''
        test to confirm if we can return a list of all contacts saved
        '''
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)

    def test_copy_email(self):
        '''
        test to confirm that we are copying the email address from a found contact
        '''
        self.new_contact.save_contact()
        Contact.copy_email("071793849")

        self.assertEqual(self.new_contact.email,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()