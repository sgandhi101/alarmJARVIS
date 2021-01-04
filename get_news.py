import feedparser


def get_news():
    rss_url = "https://foreignpolicy.com/feed/"
    rss = feedparser.parse(rss_url)

    feed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1][
        'title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + \
               rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '.  ' + rss.entries[3][
                   'description'] + '.  '

    news = " and I've curated the latest Foreign policy news from around the world.  " + str(feed)
    return news


