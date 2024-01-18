from flask import Flask,render_template,request, redirect, session
from data_base import db,Liked,Comment,User
from flask_login import LoginManager, login_user, login_required, current_user
from datetime import timedelta

def create_app():
    from auth import auth
    from main import main

    app = Flask(__name__,static_url_path='/static')
    app.config["SECRET_KEY"] = '@3FG'
    app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=3)


    app.register_blueprint(auth)
    app.register_blueprint(main)
    



    @login_manager.user_loader
    def load_user(user_id):
        from data_base import User
        return User.query.get(int(user_id))
    return app