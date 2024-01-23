from flask import Flask,render_template,request, redirect, session
from data_base import db,Liked,Comment,User
from flask_login import LoginManager, login_user, login_required, current_user
from datetime import timedelta

def create_app():
    from auth import auth
    from main import main
    from config import Config
    from .extensions import db,login_manager

    app = Flask(__name__,static_url_path='/static')

    app.config.from_object(Config())
    app.register_blueprint(auth)
    app.register_blueprint(main)

    db.init_app(app)
    login_manager.init_app(app)
    
    return app