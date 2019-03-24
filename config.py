import os
import requests
basedir = os.path.abspath(os.path.dirname(__file__))


def _get_resume_json(url, resume_files):
    json_out = {}
    for file in resume_files:
        response = requests.get(url + file + ".json")
        json_out[file] = response.json()[file]
    return json_out


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com', 'jb.jouvin@gmail.com']
    POSTS_PER_PAGE = 5
    
    RESUME_URL = "http://jbjouvin.pro.s3-website-eu-west-1.amazonaws.com/json/"
    RESUME_FILES = ["person", "skills", "techskills", "schools", "spareTime", "xp"]
    JSON_RESUME = _get_resume_json(RESUME_URL, RESUME_FILES)
