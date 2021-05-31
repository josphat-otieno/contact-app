import pyperclip
class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = [] # Empty contact list

    def __init__(self,first_name,last_name,number,email):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

    def save_contact(self):
        '''
        save contact method saves contact objects into contact_list
        '''
        Contact.contact_list.append(self)
    
    def delete_contact(self):
        '''
        delete contact method deletes contact saved from the contact list
        '''
        Contact.contact_list.remove(self)
    
    @classmethod
    def find_contact_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for contact in cls.contact_list:
            if contact.phone_number==number:
                return contact

    @classmethod
    def contact_exist(cls,number):
        '''
        a method that checks if the contact exists
        from the contact_list
        args: number and a boolean
        '''
        for contact in cls.contact_list:
            if contact.phone_number==number:
                return True
        return False

    @classmethod
    def display_contacts(cls):
        '''
        method to return the contact list
        '''
        return cls.contact_list

    @classmethod
    def copy_email(cls,number):
        contact_found=Contact.find_contact_by_number(number)
        pyperclip.copy(contact_found)


    # new_contact=Contact("josephat","Otieno","0712345678","jose@gmail.com")
    # print(new_contact.first_name)
