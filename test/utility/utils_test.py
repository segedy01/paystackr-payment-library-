from application.modules.utility.utils import isvalid_email, isvalid_phonenumber
from unittest import TestCase


class UtilsTest(TestCase):
    """
    Tests the billing class for stateless logic correctness
    """

    def setUp(self):
        """
        Initialize one time expensive operations here
        """
        pass

    def tearDown(self):
        """
        Release expensive resources
        """
        pass


    @staticmethod
    def build_email():
    	return {
		    	'email1': 'adesanyaolusegun@gmail.com',
		    	'email2': 'olusegunadesanya@live.co.uk',
		    	'email3': 'olusegun.adesanya@gmail.com',
		    	'email4': 'olusegun.adesanya@live.co.uk',
		    	'invalidemail1': 'olusegun@live',
		    	'invalidemail2': 'segun@live.',
		    	'invalidemail3': 'olusegun.com',
		    	'invalidemail4': 'olusegun@.com' 
		    	}


    @staticmethod
    def build_phone():
    	return {
		    	'phone1' : '+2347094354465',
		    	'phone2' : '2347094354465',
		    	'phone3' : '+23470943565',
		    	'phone4' : '07094354465',

		    	}


    def test_email_is_valid(self):
    	emails = self.__class__.build_email()

    	response = isvalid_email(emails.get('email1'))
    	is_email = response.popleft()
    	self.assertTrue(is_email)

    	response = isvalid_email(emails.get('email2'))
    	is_email = response.popleft()
    	self.assertTrue(is_email)

    	response = isvalid_email(emails.get('email3'))
    	is_email = response.popleft()
    	self.assertTrue(is_email)

    	response = isvalid_email(emails.get('email4'))
    	is_email = response.popleft()
    	self.assertTrue(is_email)


    def test_email_is_invalid(self):
    	emails = self.__class__.build_email()

    	response = isvalid_email(emails.get('invalidemail1'))
    	is_email = response.popleft()
    	self.assertFalse(is_email)

    	response = isvalid_email(emails.get('invalidemail2'))
    	is_email = response.popleft()
    	self.assertFalse(is_email)

    	response = isvalid_email(emails.get('invalidemail3'))
    	is_email = response.popleft()
    	self.assertFalse(is_email)

    	response = isvalid_email(emails.get('invalidemail4'))
    	is_email = response.popleft()
    	self.assertFalse(is_email)


    def test_phone_is_valid(self):
    	phone_numbers = self.__class__.build_phone()

    	response = isvalid_phonenumber(phone_numbers.get('phone1'))
    	is_phone = response.popleft()
    	self.assertTrue(is_phone)

    	esponse = isvalid_phonenumber(phone_numbers.get('phone2'))
    	is_phone = response.popleft()
    	self.assertTrue(is_phone)


    def test_phone_is_invalid(self):

    	phone_numbers = self.__class__.build_phone()


    	response = isvalid_phonenumber(phone_numbers.get('phone3'))
    	is_phone = response.popleft()
    	self.assertFalse(is_phone)



