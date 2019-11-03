from django.core.mail import send_mail as mail_sender
from django.template.loader import render_to_string
from django.conf import settings as django_settings
from apps.mailer.models import MailLog


def send_mail(*args, need_copy=False, render_kwargs={}, **kwargs):
    html_message=render_to_string(
        **render_kwargs
    )
    mail_sender(
        *args, 
        html_message=html_message,
        **kwargs
    )
    MailLog.objects.create(content=html_message, receiver_email)
