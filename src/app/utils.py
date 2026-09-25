'''
Author: Mckenna Steenbock
Description: This file creates a custom wrapper
to check user roles before they access an endpoint.
Note: The custom role wrapper was adapted from Steenbock (2025).
'''

from functools import wraps
from flask_login import current_user
from flask import abort

def role_required(role):
    def wrapper(wrap):
        @wraps(wrap)
        def decorator(*args, **kwargs):
            permitted_role = role
            if current_user.role != permitted_role:
                abort(401) #Unauthorized
            return wrap(*args, **kwargs)
        return decorator
    return wrapper
