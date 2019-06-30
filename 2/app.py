import feedparser
from flask import Flask,render_template
# The render_template function is the magic which takes a Jinja template as input and produces pure HTML

app = Flask(__name__)

# Instead of declaring global variable for each of our feeds, we'll build Python dictionary that encapsulates them all.
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

# indicate to Flask which parts of our application should be triggered by which URLs
# We still return the BBC news feed by default
@app.route('/')
@app.route('/bbc')
def bbc():
    return def_news('bbc')


@app.route('/cnn')
def cnn():
    return def_news('cnn')


@app.route('/fox')
def fox():
    return def_news('fox')


@app.route('/iol')
def iol():
    return def_news('iol')


def def_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    # The first line of this function passes the BBC feed URL to our feed parser library
    # which downloads the feed, parses it, and returns a Python dictionary

    first_article = feed['entries'][0]
    # In the this line, we grabbed just the first article from the feed and assigned it to a variable
    return """<html>
     <body>
     <h1> BBC Headlines </h1>
     <b>{0}</b> <br/>
     <i>{1}</i> <br/>
     <p>{2}</p> <br/>
     </body>
    </html>""".format(first_article.get("title"), first_article.
                      get("published"), first_article.get("summary"))

# note that feed parser may well throw an exception on attempting to parse the BBC URL.
# If your local Internet connection is unavailable, the BBC server is down, or the provided feed is malformed


if __name__ == '__main__':
    app.run()
