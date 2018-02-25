from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Softbank robotics documentation pepper proxim'it
appy = Flask(__name__)
appy.config.from_object(Config)

bootstrap = Bootstrap(appy)

db = SQLAlchemy(appy)
Migrate = Migrate(appy, db)

Login = LoginManager(appy)
Login.login_view = "login"

from app import routes, models
