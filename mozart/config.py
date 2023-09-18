import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'mail.mozartacademyofmusic.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'customer@mozartacademyofmusic.com'
    MAIL_PASSWORD = '@MozartAcademy'
    MAIL_DEFAULT_SENDER = 'mozartacademy17@gmail.com'