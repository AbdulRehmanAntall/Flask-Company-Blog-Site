from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from companyblog.models import User

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('UserName',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match')])
    pass_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=filter.data).first():
            raise ValidationError('Your email has already been registered')
        
    def check_username(self,field):
        if User.query.filter_by(username=filter.data).first():
            raise ValidationError('Your username has already been registered')
        
class UpdateUserForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('UserName',validators=[DataRequired()])
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png','jpeg'])])
    submit=SubmitField('Update')
    
    def check_email(self,field):
        if User.query.filter_by(email=filter.data).first():
            raise ValidationError('Cannot Update to this email')
        
    def check_username(self,field):
        if User.query.filter_by(username=filter.data).first():
            raise ValidationError('Cannot Update to this username')
        

    