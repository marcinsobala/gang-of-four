"""
Disabling slack messaging is trivial now. Just remove line where handlers are being set up.
Changing to different messaging system is also simple. You just need to create new listener and
set it up here. No longer do you have to sift through the functions that use it, cause they depend
only on event.
"""

from observer.api.plan import upgrade_plan
from observer.api.user import register_new_user, password_forgotten
from observer.listeners.listener_log import setup_log_event_handlers
from observer.listeners.listener_plan_upgrade import setup_plan_upgrade_handlers
from observer.listeners.listener_slack import setup_slack_event_handlers

setup_slack_event_handlers()
setup_log_event_handlers()
setup_plan_upgrade_handlers()

user_email = "email@mail.com"

print("Register user")
register_new_user("Dude", "password", user_email)

print("\nReset password")
password_forgotten(user_email)

print("\nUpgrade plan")
upgrade_plan(user_email)
