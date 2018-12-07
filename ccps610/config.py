import os


class Config:
    SECRET_KEY = '2367628bb0b13ce0c676dfde280ba245'
    
    MAIL_SERVER = 'smtp.gmail.com'
    #MAIL_PORT = 587
    #MAIL_USE_TLS = True
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    #SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')
    #MAIL_USERNAME = os.environ.get('EMAIL_USER')
    #MAIL_PASSWORD = os.environ.get('EMAIL_PASS')



    SQLALCHEMY_DATABASE_URI = 'postgres://amxdyopsspfkex:bdcc5c1d7cc43122be7e17a337a2177acf8396821db33cfddeee3e637118514e@ec2-23-21-65-173.compute-1.amazonaws.com:5432/dd3tlvdmo6j6qd'

    MAIL_USERNAME = 'jdsouza4613@gmail.com'
    MAIL_PASSWORD = 'Apple271'
