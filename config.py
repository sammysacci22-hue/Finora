import os

class Config:
    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        'development-key-change-later'
    )

    DATABASE = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'instance',
        'finora.db'
    )
