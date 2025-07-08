import threading

_user_signup_data = threading.local()

def set_signup_role(role):
    _user_signup_data.role = role

def get_signup_role():
    return getattr(_user_signup_data, 'role', None)

def clear_signup_role():
    if hasattr(_user_signup_data, 'role'):
        del _user_signup_data.role
