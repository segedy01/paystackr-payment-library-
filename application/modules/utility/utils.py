import re
from collections import deque

def isvalid_email(email):
    isvalid = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
    email_que = [email]
    if isvalid:
        email_que.insert(0, True)
        return deque(email_que)
    else:
        email_que.insert(0, False)
        return deque(email_que)

def isvalid_phonenumber(phone):
    isvalid =re.match(r'(^(\+\d{13})$)', phone)
    phone_que = [phone]
    if isvalid:
        phone_que.insert(0, True)
        return deque(phone_que)
    else:
        phone_que.insert(0, False)
        return deque(phone_que)