from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', id="uname", validators=[DataRequired()])
    password = PasswordField('Password', id="pword", validators=[DataRequired()])
    password_2fa = PasswordField('Password_2fa', id="2fa", validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', id="uname", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', id="pword", validators=[DataRequired()])
    password_2fa = PasswordField('Password_2fa', id="2fa", validators=[DataRequired()])
    # password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')
class SpellForm(FlaskForm):
    inputtext = TextAreaField('Enter text...', id='inputtext', validators=[DataRequired()])
    submit = SubmitField('Submit')
