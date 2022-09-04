import smtplib
import socket
import sys
import imapclient
import pyzmail
import pprint


def emailAddressList(receiver):
    text = receiver
    clean_text = ''
    for letter in text:
        if letter == ' ':
            continue
        else:
            clean_text += letter
    list_of_emails = clean_text.split(';')
    return list_of_emails


def SendingMails(email_address, password, subject, receiver, message):
    body = f"Subject: {subject}. \n\n {message}"
    emails = emailAddressList(receiver)
    try:
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_object.ehlo()
        smtp_object.starttls()
        smtp_object.login(email_address, password)
        if len(emails) == 1:
            send_mail_status = smtp_object.sendmail(email_address, receiver, body)
            if send_mail_status != {}:
                result = 'invalid'
            else:
                result = 'valid'
            return result
        else:
            for email in emails:
                send_mail_status = smtp_object.sendmail(email_address, email, body)
                if send_mail_status != {}:
                    result = 'invalid'
                else:
                    result = 'valid'
            return result
    except:
        result = 'invalid'
        return result

