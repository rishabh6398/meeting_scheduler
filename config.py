import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/meeting_scheduler'
    SQLALCHEMY_TRACK_MODIFICATIONS = False