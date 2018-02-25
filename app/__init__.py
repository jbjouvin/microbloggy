from flask import Flask
from flask_bootstrap import Bootstrap

appy = Flask(__name__)
bootstrap = Bootstrap(appy)

from app import routes