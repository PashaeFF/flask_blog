import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blog.extesnions import db
from blog.main.config import Config





#parol generate
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config())
    print()
    db.init_app(app)
    with app.app_context() as ctx:
        db.create_all()
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    from blog.users.routes import users
    from blog.posts.routes import posts
    from blog.main.routes import main
    from blog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    return app