from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from app.config import Config
from app.sum_routes import sum_bp
from dotenv import load_dotenv


db = SQLAlchemy()
ma = Marshmallow() 
load_dotenv() 


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

  
    db.init_app(app)
    ma.init_app(app)
  
    
    with app.app_context():
        db.create_all()

  
    app.register_blueprint(sum_bp)

    return app
