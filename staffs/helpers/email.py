from django.conf import settings
from django.core.mail import send_mail
from django.template import loader


def send_email_notification(recipients, template, context, message='Budget Team'):  # noqa E501
    # send email
    sender = settings.DEFAULT_FROM_EMAIL
    html_message = loader.render_to_string(template, context)

    send_mail(
        message=message,
        subject=message,
        from_email=sender,
        recipient_list=recipients,
        fail_silently=True,
        html_message=html_message
    )
