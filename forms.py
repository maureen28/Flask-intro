from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=25)])
    email= StringField('Email', validators=[DataRequired(),Email() ])
    password = PasswordField('Enter password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('SignUp')
    
    
    
class LoginForm(FlaskForm):
    email= StringField('Email', validators=[DataRequired(),Email() ])
    password = PasswordField('Enter password', validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Rememeber Me')
    submit= SubmitField('Login')