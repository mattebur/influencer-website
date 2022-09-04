from influencer import app
from flask import render_template, request, flash
from influencer.forms import GmailAccountForm
from influencer.my_functions import SendingMails


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/twitter')
def twitter_page():
    return render_template('twitter.html')


@app.route('/gmail', methods=['GET', 'POST'])
def gmail_page():
    form = GmailAccountForm()
    if form.validate_on_submit():
        mail_to_send = SendingMails(email_address=form.email_address.data,
                                     password=form.password.data,
                                     receiver=form.receiver.data,
                                     subject=form.subject.data,
                                     message=form.message.data)
        if mail_to_send == 'valid':
            flash('Message sent', category='success')
        else:
            flash('There were problems with sending email, try again', category='danger')

    return render_template('gmail.html', form=form)
