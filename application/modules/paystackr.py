import json
import os
from . import BasePayStackr
from exceptions import *
import requests
from constants.utils_constants import *


_SECRET_KEY = os.environ.get('SECRET_KEY') or "th1s ls @ $ecr3t k3y"


class PayStackr(BasePayStackr):
    """
        Implementation of The Base Class as Paystack.
    """


    def __init__(self, authentication_token=None):
        self.authentication_token = authentication_token
        if not self.authentication_token:
            self.authentication_token = _SECRET_KEY
            if not self.authentication_token:
                raise FailedAuthentication("Get an authentication token")

    def method_calls(self, method, url, payload=None):
        """
            The Rasen Shuriken HTTP Method. Allows only reasonable http calls
            when all the right parameters are provided. Its an easy to use method

            :param method: HTTP_METHOD (Get, Post .....)
            :param url: a valid url (https://letsgowinasoul. dazzall)
            :param payload: payload to be sent to the above url. do you know json kungfu?
            :return: A tuple that consist of status code, message, and a body.
        """

        self.payload = payload
        self.url = url
        http_method = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'PATCH': requests.patch,
            'DELETE': requests.delete
        }

        self.get_method = str(method).upper()
        if self.get_method not in http_method:
            raise InvalidHTTPMethod("Check Python requests documentation for ")
        method_call = http_method.get(self.get_method)
        response = method_call(headers=self.set_header(), data=self.payload)
        if not response:
            raise InvalidPayload("Payload Man!! You gave a wrong load")
        return response.status_code, response.message, response.data

    def set_header(self, **kwargs):
        """
            I work where theres no BR so a lot of **kwargs and *args.
            **Kwargs for unseen situations
            :param kwargs:
            :return: A dict
        """
        if kwargs:
            if not isinstance(kwargs, dict):
                raise InvalidType("K for keyword argument **Kwargs only; read python Documentation")

            header =  {
                    "Content-Type": MIME_TYPE,
                    "Authorization": "Bearer " + self.authentication_token,
                    }
            header = header.update(kwargs)
            return header
        return {
            "Content-Type": MIME_TYPE,
            "Authorization": "Bearer " + self.authentication_token,
        }