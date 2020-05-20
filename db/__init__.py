from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


def init():
    """init
    """
    DB.create_all()
