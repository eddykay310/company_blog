from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from blog.models import User

# Different form classes
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password_confirm',message='password must match')])
    password_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already taken!')
    
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already taken!')

class UpdateUserForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    profile_picture = FileField('Update Your Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already taken!')
    
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already taken!')
    