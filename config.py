import os

basedir = os.path.abspath(os.path.dirname(__file__))
# C:\\Users\\emili\\....\\ECFFX\\price_tracker_app

class Config:
    AUTH = os.environ.get('AUTH')
    AUTH2 = os.environ.get('AUTH2')
    # DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'app.db')