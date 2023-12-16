from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#data required: user must input some data, can't leave blank
#Length: input must be between min and max
#Email: input must be a valid email
#EqualTo: input must be equal to parameter

class RegistrationForm(FlaskForm):

    username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):

    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    #allows users to stay logged in for some time after browser closes
    remember = BooleanField('Remember Me') #BooleanField --> checkbox
    
    submit = SubmitField('Login')