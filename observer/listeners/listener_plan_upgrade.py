from observer.event import subscribe


def handle_user_upgrade_plan_event(user):
    print(f"L_PLAN: User with email address {user.email} has upgraded their plan to {user.plan}")


def setup_plan_upgrade_handlers():
    subscribe("user_plan_upgrade", handle_user_upgrade_plan_event)
