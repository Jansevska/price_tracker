from flask import Flask
from config import Config


# Create an instance of Flask class
app = Flask(__name__)


# Configuring our app with Attributes and Values from the Config class --> CREATED AFTER CREATION OF FORMS!!!! <-- app.config['SECRET_KEY'] = 'you-will-never-guess > moved to config.py folder!
# app.config.from_object(Config)
app.config.from_object(Config)


# Create an instance of SQLAlchemy to represent our database
db = ...(app) # the app as instance of Flask
# Create an instance of migrate to track our database migrations
migrate = ...(app, db)

# register the api blueprint with our app
# from .blueprints.api import api
# app.register_blueprint(api)

# import routes
from . import routes