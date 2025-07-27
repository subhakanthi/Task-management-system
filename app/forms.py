from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Repeat Password', 
                             validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description')
    priority = SelectField('Priority', 
                          choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
                          default='medium')
    category = SelectField('Category',
                          choices=[('personal', 'Personal'), ('work', 'Work'), 
                                 ('shopping', 'Shopping'), ('health', 'Health')],
                          default='personal')
    due_date = DateField('Due Date', format='%Y-%m-%d')
    submit = SubmitField('Save Task')