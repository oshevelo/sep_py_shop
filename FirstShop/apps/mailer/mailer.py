from django.core.mail import send_mail as mail_sender
from django.template.loader import render_to_string
from django.conf import settings as django_settings


def send_mail(*args, need_copy=False, render_kwargs={}, **kwargs):
    mail_sender(
        *args, 
        html_message=render_to_string(
            **render_kwargs
        ),
        **kwargs
    )
