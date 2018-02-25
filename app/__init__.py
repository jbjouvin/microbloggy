from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

appy = Flask(__name__)
bootstrap = Bootstrap(appy)
appy.config.from_object(Config)

from app import routes