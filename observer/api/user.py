"""
Functions now do one thing and post event to handle by event handlers. Number of imports
shrinks significantly.
"""

from uuid import uuid4

from observer.fake_db import create_user, find_user
from observer.event import post_event



def register_new_user(name: str, password: str, email: str):
    # create an entry in the database
    user = create_user(name, password, email)

    post_event("user_registered", user)


def password_forgotten(email: str):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = str(uuid4())

    post_event("user_password_forgotten", user)
