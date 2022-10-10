"""
If you want to temporarily disable logs for user_registered event, just don't subscribe to it
"""

from observer.event import subscribe


def handle_user_registered_event(user):
    print(f"L_LOG: {user.name} has registered with email address {user.email}")


def handle_user_password_forgotten_event(user):
    print(f"L_LOG: User with email address {user.email} requested a password reset")


def handle_user_upgrade_plan_event(user):
    print(f"L_LOG: User with email address {user.email} has upgraded their plan to {user.plan}")


def setup_log_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    subscribe("user_plan_upgrade", handle_user_upgrade_plan_event)
