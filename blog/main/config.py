import os

# class Config:
#     SECRET_KEY = 'cc7dd89bb73a653fecd5364b4eba3c1a'
#     #app.config["SQLALCHEMY_TRACK_M ODIFICATIONS"] = False #Tural dedi gelecekde bele olacaq)))
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
#     MAIL_SERVER = 'smtp.gmail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = 'pashayevler@gmail.com'
#     MAIL_PASSWORD = 'pugwsgasttimbzoj' 
    
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY',default='cc7dd89bb73a653fecd5364b4eba3c1a')
    #app.config["SQLALCHEMY_TRACK_M ODIFICATIONS"] = False #Tural dedi gelecekde bele olacaq)))
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',default='sqlite:///site.db')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME',default='')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD',default='')