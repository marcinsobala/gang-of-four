import dataclasses

db_users = []


@dataclasses.dataclass
class User:
    name: str
    password: str
    email: str
    plan: str = "basic"
    reset_code: str = ""

    def reset_password(self, code: str, new_pass: str):
        if code != self.reset_code:
            raise Exception("Invalid password reset code")
        self.password = new_pass


def create_user(name: str, password: str, email: str):
    user = User(name, password, email)
    db_users.append(user)
    return user


def find_user(email: str):
    try:
        return next(x for x in db_users if x.email == email)
    except StopIteration:
        raise Exception("User does not exist")