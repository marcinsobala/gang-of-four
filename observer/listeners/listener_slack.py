from observer.event import subscribe


def handle_user_registered_event(user):
    print(f"L_SLACK: {user.name} has registered with email address {user.email}. SPAM this person!")


def handle_plan_upgrade_event(user):
    print(f"L_SLACK: User with email address {user.email} has upgraded their plan to {user.plan}")


def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_plan_upgrade", handle_plan_upgrade_event)
