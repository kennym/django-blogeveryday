from appengine_django.models import BaseModel
from google.appengine.ext import db

from subscription import utils

class Subscriber(db.Model):
    user = db.UserProperty()
    join_date = db.DateProperty(auto_now_add=True)

    blog_url = db.LinkProperty(verbose_name="Blog URL")
    feed_url = db.LinkProperty(verbose_name="Feed URL")

    entry_count = db.IntegerProperty()
    last_entry = db.DateTimeProperty()

    # Miscellaneous properties
    confirm_notification_sent = db.BooleanProperty(default=False)
    welcome_notification_sent = db.BooleanProperty(default=False)

    def check_for_new_entries(self):
        since_datetime = self.last_entry
        if not since_datetime:
            since_datetime = self.join_date
        entry_count, last_entry = utils.get_new_entries(self.last_entry, self.feed_url)
        self.entry_count += entry_count
        self.last_entry = last_entry

        # Save the new data
        self.save()

    def save(self):
        if not self.feed_url:
            feed_url = parser.parse_feed_uri_from(self.blog_url)
            if not feed_url:
                # Notify the user that he should supply his feed URL.
                pass
            else:
                self.feed_url = feed_url
        super(Subscriber, self).save()
