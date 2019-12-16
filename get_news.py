#!/usr/bin/env python
import feedparser

def getNews():
    rss_url = "https://foreignpolicy.com/feed/"
    rss = feedparser.parse(rss_url)

    newsfeed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1][
    'title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + \
           rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '.  ' + rss.entries[3][
               'description'] + '.  '

# print newsfeed
    newsfeed = newsfeed.encode('utf-8')

# Today's news from BBC
    news = "and I've curated the latest Foreign policy news from around the world.  " + newsfeed
    return news

print getNews()