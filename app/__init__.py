from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize your database and migrate objects outside of create_app
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Bind the SQLAlchemy db object to this specific Flask app
    db.init_app(app)
    # Bind the Migrate object to the app and db
    migrate.init_app(app, db)
    
    # You no longer need 'db.create_all()' if you're using Flask-Migrate
    # with app.app_context():
    #     db.create_all()  # Remove this when using Flask-Migrate

    # Import and register your blueprint
    from .routes import main as main_blueprint  # Adjust 'yourapplication' as per your project structure
    app.register_blueprint(main_blueprint)
    
    return app

