from data_base import db, User 
from flask import redirect,render_template
from flask_login import login_user, login_required
from . import auth

@auth.route('/register', methods=['POST','GET'])
def regist_page():
    from .forms import MyForm
    form = MyForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect('/HOME')
    return render_template('auth/registration.html',form=form)
@auth.route('/login', methods=['POST','GET'])
def login_page():
    from .forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        print(user)
        if not user or user.password != form.password.data:
            print("Usern not found")
            # login_page
            return render_template('auth/login.html',form=form,error = "Invalid uesr or password")
        login_user(user, remember = True)  
        return redirect('/HOME')
    return render_template('auth/login.html',form=form)
@login_required  
def profil() :
    movies = current_user.liked_movies

    return render_template('profile.html',movies=movies)
