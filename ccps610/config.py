import os


class Config:
    SECRET_KEY = '2367628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')
    MAIL_SERVER = 'smtp.gmail.com'
    #MAIL_PORT = 587
    #MAIL_USE_TLS = True
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')