import os

class Config:

    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'WAGWANGANJAMANNEVERDIES'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    
    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config): 
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}