users: list[str] = ['Alice', 'Bob', 'Charlie']


def get_users() -> list[str]:
    return users


def create_user(username: str) -> None:
    users.append(username)

