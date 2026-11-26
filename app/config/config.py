import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.getenv("FLASK_ENV")
    DEBUG = True if FLASK_ENV == "development" else False
    APPLICATION_NAME = os.getenv("APPLICATION_NAME")
