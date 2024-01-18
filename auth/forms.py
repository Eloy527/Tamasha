from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,EmailField
from wtforms.validators import DataRequired,Regexp,Email,ValidationError


def validators_username(form, username):
    from data_base import User
    user = User.query.filter_by(username = username.data).first()
    if user:
        raise ValidationError("usernamem already is us")
def validators_email(form, email):
    from data_base import User
    user = User.query.filter_by(email = email.data).first()
    if user:
        raise ValidationError("email already is us")

class MyForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), validators_username])
    email = EmailField('email', validators=[DataRequired(), Email(), validators_email])
    password = PasswordField('password', validators=[DataRequired(), Regexp(r"(?=.*[a-z])(?=.*[A-Z]+)(?=.*\d)(?=.*[!@#$%&._/])[a-zA-Z\d!@#$%&._/]{8,}",message="Wrong password")])
    checkbox = BooleanField('I Agree to Privacy Policy')
class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Regexp(r"(?=.*[a-z])(?=.*[A-Z]+)(?=.*\d)(?=.*[!@#$%&._/])[a-zA-Z\d!@#$%&._/]{8,}",message="Wrong password")])
