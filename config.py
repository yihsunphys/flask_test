import os

basedir = os.path.abspath(os.path.dirname(__file__))    

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-longand-secure-key'

    # RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'A-very-long-and-secure-key'
    # RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or 'A-very-long-secret-key'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False