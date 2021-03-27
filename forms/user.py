from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, \
    IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField(
        'Password',
        validators=[DataRequired(),
                    Length(min=4, max=100,
                           message="Пароль должен быть от 4 до 100 символов")])
    password_again = PasswordField(
        'Repeat password',
        validators=[DataRequired(),
                    EqualTo('password', message="Пароли не совпадают")])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')
