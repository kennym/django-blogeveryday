# -*- mode: python; coding: utf-8; -*-

"""
Parser for feeds using the feedparser (www.feedparser.org) library.
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from subscription.lib import feedparse

import logging
from datetime import datetime

def get_feed_entries_from(feed_uri):
    logging.info("Getting and parsing feed: " + feed_uri)

    d = feedparse.parse(feed_uri)
    return d
