"""
Holds code constants for easy tracking and lookup
"""

HTTP_GOOD_REQUEST = 200  #: You did a Good job, so We did a good job. Give us more requests like this
HTTP_CREATED = 201   #: We have created the resource you wanted us to create
HTTP_ACCEPTED = 202  #: Your request is with us, We have agreed to work on it when we can
HTTP_BAD_REQUEST = 400   #: Your request is a crime against http
HTTP_UNAUTHORIZED = 401  #: Are you sure you are authenticated
HTTP_NOT_FOUND = 404  #: You are looking for aliens or something else that does not exist
HTTP_NOT_ALLOWED = 405   #: No no no, that is not part of our agreement
HTTP_TIMEOUT = 408   #: We ran out of patience with your request
HTTP_PRECONDITION_FAILED = 412
HTTP_UNSUPPORTED_MEDIA_TYPE = 415    #: Bad content type
HTTP_UNPROCESSABLE_ENTITY = 422  #: Nice work but you are spitting garbage
HTTP_NOT_IMPLEMENTED = 501   #: The action is not implemented on this server
HTTP_BAD_GATEWAY = 502   #: Backend service is not available
HTTP_SERVICE_UNAVAILABLE = 503  #: Self provided service is not available
HTTP_GATEWAY_TIMEOUT = 504  #: We could not wait for a response because our time and your time is valuable to us


__all__ = [
    'HTTP_GOOD_REQUEST',
    'HTTP_CREATED',
    'HTTP_ACCEPTED',
    'HTTP_BAD_REQUEST',
    'HTTP_UNAUTHORIZED',
    'HTTP_NOT_FOUND',
    'HTTP_NOT_ALLOWED',
    'HTTP_TIMEOUT',
    'HTTP_PRECONDITION_FAILED',
    'HTTP_UNSUPPORTED_MEDIA_TYPE',
    'HTTP_UNPROCESSABLE_ENTITY',
    'HTTP_NOT_IMPLEMENTED',
    'HTTP_BAD_GATEWAY',
    'HTTP_SERVICE_UNAVAILABLE',
    'HTTP_GATEWAY_TIMEOUT'
]
