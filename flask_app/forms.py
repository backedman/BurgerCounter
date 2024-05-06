from ast import Pass
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, TextAreaField, PasswordField,IntegerField
from wtforms.validators import (
    InputRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
    NumberRange
)

from .models import User

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=30)])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
    
class BurgerForm(FlaskForm):
    
    Buns = IntegerField('Buns', validators=[InputRequired(), NumberRange(min=2)])
    
    Patties = IntegerField('Patties', validators=[InputRequired()])
    
    Lettuce = IntegerField('Lettuce', validators=[InputRequired()])
    
    Tomato = IntegerField('Tomato', validators=[InputRequired()])
    
    submit_burger = SubmitField("Order Burger")
    
class UpdatePasswordForm(FlaskForm):
    
    curr_password = StringField("Current Password", validators=[InputRequired(), Length(min=1)])
    
    new_password = StringField("New Password", validators=[InputRequired(), Length(min=1)])
    
    conf_password = StringField("Confirm Password", validators=[InputRequired(), Length(min=1), EqualTo("new_password")])

    submit_password = SubmitField("New Password")