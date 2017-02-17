
from exceptions import *

not_implemented_message = "Method is yet to be implement"

class BasePayStackr():
    """
        Base class for paystackr. It implement the Skelenton of the main classes
        and inherited from. no method is called implemented directly in the base class

        Args:
            authentication_token: this is usually in the os environ or can be passed in to
            initialise the class
    """

    def __init__(self, authentication_token=None, *args, **kwargs):
        raise NotImplementedError("This is an abstract base class")


    def method_calls(self, method, payload):

        """
        This implement a general http method that can be relied upon
        to perform http request
        :param method: HTTP_Method
        :return: dictionary (JSON)
        """
        raise NotImplementedError(not_implemented_message)

    def set_header(self, header_data):
        """
            builds the header

            :param header_data: a dictionary
            :return: a dict as header
        """
        raise NotImplementedError(not_implemented_message)