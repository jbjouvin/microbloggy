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

import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

if not appy.debug:
    if appy.config['MAIL_SERVER']:
        auth = None
        if appy.config['MAIL_USERNAME'] or appy.config['MAIL_PASSWORD']:
            auth = (appy.config['MAIL_USERNAME'], appy.config['MAIL_PASSWORD'])
        secure = None
        if appy.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(appy.config['MAIL_SERVER'], appy.config['MAIL_PORT']),
            fromaddr='no-reply@' + appy.config['MAIL_SERVER'],
            toaddrs=appy.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        appy.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import routes, models, errors

