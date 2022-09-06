from influencer import app
from flask import render_template, request, flash
from influencer.forms import GmailAccountForm, TwitterAccountForm
from influencer.my_functions import SendingMails, TweetAPost



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/twitter', methods=['GET', 'POST'])
def twitter_page():
    form = TwitterAccountForm()
    if form.validate_on_submit():
        tweet = TweetAPost(access_token=form.access_token.data,
                           access_secret=form.access_token_secret.data,
                           message=form.message.data)
        if tweet == 'valid':
            flash('Tweet posted', category='success')
        else:
            flash('Something went wrong', category='danger')
    return render_template('twitter.html', form=form)


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
