import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = "True"
    MAIL_USERNAME = "kaberiaharmony@gmail.com"
    MAIL_PASSWORD = "rbmfogqizwealjkv"