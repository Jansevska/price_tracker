import os

basedir = os.path.abspath(os.path.dirname(__file__))
# C:\\Users\\emili\\....\\ECFFX\\price_tracker_app

class Config:
    # AUTH = os.environ.get('AUTH')
    AUTH = os.environ.get('AUTH')
    
    # Secret key for signing cookies
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # Database configuration
    # The SQLALCHEMY_DATABASE_URI is important for connecting to your database
    # It is typically a URL that gives details like database type, driver, user, password, hostname, port, and database name
    # For SQLite, it's just the location of the database file
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///prices.db'
    
    # This configuration helps to silence the deprecation warning from SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
