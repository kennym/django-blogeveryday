# -*- mode: python; coding: utf-8; -*-

from django.core.mail import send_mail
from django.db.models.signals import pre_save

import subscription.models

def send_confirm_notification(sender, **kwargs):
    if sender.confirm_notification_sent is False:
        pass
pre_save.connect(send_confirm_notification, sender=subscription.models)


def send_welcome_notification(sender, **kwargs):
    if sender.welcome_notification_sentf is False:
        body = """
You have successfully signed up for EveryDayBlogging!

Have fun and don't forget to start writing!

Your EveryDayBlogging Team
"""
        send_mail("Your Registration on EveryDayBlogging.com",
                  body, "admin@everydayblogging.com", sender.user.email(),
                  fail_silently=False)

pre_save.connect(send_welcome_notification, sender=subscription.models)
