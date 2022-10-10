"""
In order to change what's done after user upgrades
his plan you'd have to delve deep into function insides.
"""

from observer.fake_db import find_user
from slack import post_slack_message
from email import send_email
from logs import log


def upgrade_plan(email: str):
    # find user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    # post a Slack message to sales department
    post_slack_message(
        "sales",
        f"{user.name} has upgraded their plan"
    )

    # send a thank-you email
    send_email(
        user.name,
        user.email,
        "Thanks",
        f"Thanks for upgrading, {user.name}!"
    )

    # write server log
    log(f"{user.email} user upgraded his plan")
