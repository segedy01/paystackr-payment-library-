"""
    Customer Class
"""
from application.constants.utils_constants import *
from application.modules.utility.utils import isvalid_email, isvalid_phonenumber
from .exceptions import *
from paystackr import PayStackr
import re



class CustomerAccount(PayStackr):

    def create_customer(self, customer_payload, **kwargs):
        """

        :param email:
        :param firstname:
        :param lastname:
        :param phonenumber:
        :param kwargs:
        :return:
        """
        if customer_payload:

            deq_email = isvalid_email(customer_payload['email'])
            isemail = deq_email.popleft()
            if not isemail:
                raise EmailError("Get a valid email")
            self.email = deq_email.popleft()
            print self.email
            self.firstname = str(customer_payload['first_name'])
            self.lastname = str(customer_payload['last_name'])
            #give me number in +234********** format
            #if you like dont give me
            #you wont pass
            deq_phone = isvalid_phonenumber(customer_payload['phone'])
            isphone = deq_phone.popleft()
            if not isphone:
                raise EmailError("Give me a string and make sure it conform to +234**********")
            self.phonenumber = deq_phone.popleft()
            print self.phonenumber

        else:
            raise InvalidPayload('customer information required')

        payload = {
            "email": self.email,
            "first_name": self.firstname,
            "last_name": self.lastname,
            "phone": self.phonenumber
        }

        url = Base_API + "/customer"
        response = self.method_calls(POST, url, payload)
        return response


    def get_customer(self, customer_id):
        """
            function gets a customer in the

            :param customer_id: a unique identification related 
                                to a customer
            :Return dictionary containing customer's information
        """

        url = Base_API +'/customer/' +str (customer_id)
        response = self.method_calls(GET, url)
        return response       


    def update_customer(self, customer_id, payload):

        if payload:
            update_load = {}
            # if payload['phone']:
            #     update_load.update({'phone':payload['phone']})
            # if payload['first_name']:
            #     update_load.update({'first_name':payload['first_name']})
            # if payload['email']:
            #     update_load.update({'email':payload['email']})
            # if payload['last_name']:
            #     update_load.update({'last_name':payload['last_name']})
            keyword = ['email', 'last_name', 'first_name', 'phone']
            for key in payload:
                if key in keyword:
                    update_load.update({key:payload[key]})
            if not update_load:
                 raise InvalidPayload('provide proper key to value pair')

        else:
            raise InvalidPayload('Provide Customer information please')


        print update_load
        url = Base_API + '/customer/' + str(customer_id)
        response = self.method_calls(PUT, url, update_load)
        return response


    def get_all_customer(self):

        url = Base_API + '/customer'
        response = self.method_calls(GET, url)
        return response


    def black_white_list_customer(self, customer, action):

        action_list = ['allow', 'deny']

        if action not in action_list:
            raise InvalidPayload('The action provided is an invalid action')
        payload = {
            'customer': str(customer),
            'risk_action': action
        }

        url = Base_API + '/customer/set_risk_action'
        response = self.method_calls(POST, url, payload)
        return response