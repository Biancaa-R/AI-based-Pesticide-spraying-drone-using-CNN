from wtforms import StringField,PasswordField,SubmitField,BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import Length,DataRequired,Email,EqualTo

class RegistrationForm(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    #very very imp: the equal to arg is the variable not the label name!
    submit=SubmitField("Signup")


class LoginForm(FlaskForm):
    #username=StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField("Remember me")
    #stay logged in for sometime using a cookie! go bake cookies 
    submit=SubmitField("Login")
    #secret key for not modifying cookies, cross site requests, forgery attacks 

