from flask import current_app
from flask_mail import Message
from flask import render_template
from app import mail

def send_reset_password_mail(user, token):
    msg = Message('Password Reset Request',
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[user.email],
                  html = render_template('reset_password_mail.html', user=user, token = token))
    
    mail.send(msg)