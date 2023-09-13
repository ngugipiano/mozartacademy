from flask import Flask
from mozart.config import Config
from flask_mail import Mail


mail = Mail()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    mail.init_app(app)
    from mozart.BLUEPRINT.routes import main

    app.register_blueprint(main)
    

    return app