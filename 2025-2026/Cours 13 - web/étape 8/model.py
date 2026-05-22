import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name('users.db')


def _connect() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


# Initialiser la base SQLite au démarrage du module
with _connect() as conn:
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
        '''
    )
    count = conn.execute('SELECT COUNT(*) FROM users').fetchone()[0]
    if count == 0:
        conn.executemany(
            'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
            [
                ('bob', 'bob.doe@orange.fr', 'my_password'),
                ('alice', 'alice.smith@gmail.com', 'azerty123!'),
                ('charlie', 'charlie.dupont@yahoo.fr', 'pass-word_42'),
            ],
        )


def get_users() -> list[list[str]]:
    with _connect() as conn:
        rows = conn.execute(
            'SELECT username, email, password FROM users ORDER BY id'
        ).fetchall()
    return [[row[0], row[1], row[2]] for row in rows]


def create_user(username: str, email: str, password: str) -> None:
    with _connect() as conn:
        conn.execute(
            'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
            (username, email, password),
        )


def check_user_credentials(username: str, password: str) -> bool:
    with _connect() as conn:
        row = conn.execute(
            'SELECT password FROM users WHERE username = ?',
            (username,),
        ).fetchone()
    return row is not None and row[0] == password
