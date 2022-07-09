import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///databases/test.db"
