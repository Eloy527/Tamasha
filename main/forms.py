from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,EmailField
from wtforms.validators import DataRequired,Regexp,Email,ValidationError
from wtforms.widgets import TextArea



class CommentForm(FlaskForm):
    content = StringField('Comment', validators=[DataRequired()],widget = TextArea())
    