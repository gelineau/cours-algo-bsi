users: list[list[str]] = [
    ['bob', 'bob.doe@orange.fr', 'my_password'],
    ['alice', 'alice.smith@gmail.com', 'azerty123!'],
    ['charlie', 'charlie.dupont@yahoo.fr', 'pass-word_42'],
]


def get_users() -> list[list[str]]:
    return users


def create_user(username: str, email: str, password: str) -> None:
    users.append([username, email, password])

