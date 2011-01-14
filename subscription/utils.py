# -*- mode: python; coding: utf-8; -*-

from datetime import datetime
from subscription.lib.parser import feedparser
from subscription.lib.parser.uriparser import parse_feed_uri_from

def get_new_entries(since_datetime, feed_uri):
    """
    Parse new entries from feed_uri, which are newer than `since_datetime`.

    :since_datetime a datetime.datetime object
    :feed_uri the valid URI of the feed
    :returns a tuple
    """
    entries = feedparser.get_feed_entries_from(feed_uri)

    entry_count = 0
    for entry in entries:
        t = entry.date_parsed
        entry_date = datetime(
            year        = t[0],
            month       = t[1],
            day         = t[2],
            hour        = t[3],
            minute      = t[4],
            second      = t[5],
            microsecond = t[6]
            # FIXME:
            #tzinfo      = t[7]
        )

        if entry_date > since_datetime:
            entry_count += 1

    t = entries[0].date_parsed
    last_entry = datetime(
        year        = t[0],
        month       = t[1],
        day         = t[2],
        hour        = t[3],
        minute      = t[4],
        second      = t[5],
        microsecond = t[6]
    )

    import pdb; pdb.set_trace()

    return (entry_count, last_entry)

