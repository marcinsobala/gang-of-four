"""
Functions have low cohesion. They do too many different things and have too many
dependencies because of that

"""

from uuid import uuid4

from observer.fake_db import create_user, find_user
from slack import post_slack_message
from email import send_email
from logs import log


def register_new_user(name: str, password: str, email: str):
    # create an entry in the database
    user = create_user(name, password, email)

    # post a Slack message to sales department
    post_slack_message(
        "sales",
        f"{user.name} registered with email {user.email}. SPAM him!"
    )

    # send a welcome email
    send_email(
        user.name,
        user.email,
        "Welcome",
        f"Thanks for registering, {user.name}!"
    )

    # write server log
    log(f'user registered with email address {user.email}')


def password_forgotten(email: str):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = str(uuid4())

    # send a password reset message
    send_email(
        user.name,
        user.email,
        "Reset your password",
        f"Use your code to reset password {user.reset_code}",
    )

    # write server log
    log(f"User with email address {user.email} requested a password reset")