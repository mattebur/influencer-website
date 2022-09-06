from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Email, DataRequired, ValidationError, Length
from influencer.my_functions import SendingMails


class GmailAccountForm(FlaskForm):
    email_address = StringField(label='Your Email Address', validators=[DataRequired()])
    password = PasswordField(label='Your Gmail Password', validators=[Length(min=6), DataRequired()])
    subject = StringField(label='Subject', validators=[DataRequired()])
    receiver = StringField(label='Add receiver separated by ;', validators=[DataRequired()])
    message = TextAreaField(label='Enter your message here', validators=[DataRequired()])
    submit = SubmitField(label='Send Email')


class TwitterAccountForm(FlaskForm):
    access_token = PasswordField(label='Access Token', validators=[DataRequired()])
    access_token_secret = PasswordField(label='Access Secret Token', validators=[DataRequired()])
    message = TextAreaField(label='Message to Tweet', validators=[DataRequired()])
    submit = SubmitField(label='Tweet')
