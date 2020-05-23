from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError
from todoapp.models import User

class RegisterForm( FlaskForm ):
    username = StringField('Username', validators=[DataRequired(), Length(min=8,max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password =  PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('This username was taken. Please, take another one')
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('This email address was taken. Please, take another one')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password =  PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember me',default=False)
    submit = SubmitField('Login')