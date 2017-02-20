"""
    Customer Class
"""
from constants.utils_constants import *
from modules.utility.utils import isvalid_email, isvalid_phonenumber
from .exceptions import *
from paystackr import PayStackr
import re



class CustomerAccount(PayStackr):

    def create_customer(self, email=None, firstname=None, lastname=None, phonenumber=None, **kwargs):
        """

        :param email:
        :param firstname:
        :param lastname:
        :param phonenumber:
        :param kwargs:
        :return:
        """
        deq_email = isvalid_email(email)
        isemail = deq_email.popleft()
        if not isemail:
            raise EmailError("Get a valid email")
        self.email = deq_email.popleft()
        self.firstname = str(firstname)
        self.lastname = str(lastname)
        #give me number in +234********** format
        #if you like dont give me
        #you wont pass
        deq_phone = isvalid_phonenumber(phonenumber)
        isphone = deq_phone.popleft()
        if not isphone:
            raise EmailError("Give me a string and make sure it conform to +234**********")
        self.email = deq_email.popleft()
        self.phonenumber = phonenumber
        payload = {
            "email": self.email,
            "firstname": self.phonenumber,
            "lastname": self.lastname,
            "phonenumber": self.phonenumber
        }
        url = Base_API + "/customer"
        response = self.method_calls(POST, url, payload)
        return response