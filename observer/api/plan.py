from observer.fake_db import find_user
from observer.event import post_event


def upgrade_plan(email: str):
    # find user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    post_event("user_plan_upgrade", user)
