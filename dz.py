from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


def email(recipient_list=None):
    subject = 'Domashka na otpravky pisma '
    email_from = settings.EMAIL_HOST_USER

    template = get_template('send_email.html')

    send_mail(subject, email_from, recipient_list,
              html_message=template.render())
