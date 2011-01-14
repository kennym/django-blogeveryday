# -*- mode: python; coding: utf-8; -*-

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

import logging
import urllib2
import re
from subscription.lib.BeautifulSoup import BeautifulSoup


def parse_feed_uri_from(url):
    """
    Filter the Atom feed from the blog.
    """
    logging.info("Getting page...")
    page = urllib2.urlopen(url).read()
    logging.info("Parsing...")
    soup = BeautifulSoup(page)

    feed_uri = soup.findAll('link', type=re.compile("atom\+xml"))
    if feed_uri != []:
        feed_uri = feed_uri[0].get('href')
        logging.info("Feed URI: " + feed_uri)

        return feed_uri
    logging.warning("No feed URI found...")
    return None

if __name__ == "__main__":
    print "Parsing feed URI from URL..."
    parse_feed_uri_from('http://kennymeyer.blogspot.com')
