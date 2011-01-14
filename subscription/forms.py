# -*- mode: python; coding: utf-8; -*-

from google.appengine.ext.db import djangoforms

from subscription.models import Subscriber


class SubscriberForm(djangoforms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = ["user", "feed_url", "last_entry", "entry_count",
                   "welcome_notification_sent", "confirm_notification_sent"]
