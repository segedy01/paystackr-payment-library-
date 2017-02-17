"""
    Tastes like shit, smells like shit, looks like shit
    we shall call thee!!!
"""
class PaystackrError(Exception):
    """
        base exception class for paystackr method calls
        other exception inherits from this clas
    """
    pass


class FailedAuthentication(PaystackrError):
    """
        Handles authentication error. inherits from Paystackr
    """
    pass


class EmailError(PaystackrError):
    """
        raised when an invalid or empty email is detected
    """
    pass

class MethodNotImplemented(PaystackrError):
    """
        default error for unimplemented methods calls
    """

class InvalidHTTPMethod(PaystackrError):
    """
        Exception raised when an invalid http method is called
    """

class InvalidType(PaystackrError):
    """
        for any data type not expected
    """
class InvalidPayload(PaystackrError):
    """
        raised when nothing is returned
    """