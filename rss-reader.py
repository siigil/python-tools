# A very basic CLI based RSS Reader.
# Spits all results out to the stdout based on provided .opml file.
# Nothing fancy, just a toy to familiarize with RSS operations.
# Usage: ./python rss-reader.py <your-feed.opml>

import feedparser
import xml.etree.ElementTree as ET
import sys

def fetch_and_parse_rss(url):
    return feedparser.parse(url)

def display_feed(feed):
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print(f"Summary: {entry.summary}")
        print("-" * 40)  # Separator

def parse_opml(opml_file):
    tree = ET.parse(opml_file)
    root = tree.getroot()
    feed_urls = []

    for outline in root.iter('outline'):
        url = outline.get('xmlUrl')
        if url:
            feed_urls.append(url)

    return feed_urls

def main():
    opml_file = sys.argv[1]  # Provide on CLI
    feed_urls = parse_opml(opml_file)
    for url in feed_urls:
        feed = fetch_and_parse_rss(url)
        display_feed(feed)

if __name__ == "__main__":
    main()