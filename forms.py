from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Email,EqualTo,Length

class RegisterForm( FlaskForm ):
    username = StringField('Username', validators=[DataRequired(), Length(min=8,max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password =  PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo(password)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=8,max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password =  PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember me',default=False)
    submit = SubmitField('Login')