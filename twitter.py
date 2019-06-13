#     Small Twitter scraper in Python
#     Currently only grabs the first 20 tweets on a public profile, without API access
#     Trying to figure out how to not use that and grab tweets where possible
#     Make sure BeautifulSoup is installed when using Python

import requests
from bs4 import BeautifulSoup

all_tweets = []
url = 'https://twitter.com/raxcodes'
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
timeline = html.select('#timeline li.stream-item')
saveTweet = open("savedTweet2.txt", "a")

for tweet in timeline:
    tweet_id = tweet['data-item-id']
    tweet_text = tweet.select('p.tweet-text')[0].get_text()
    printTweet = {"id": tweet_id, "text": tweet_text}
    saveTweet.writelines(str(printTweet))
    saveTweet.write("\n")

saveTweet.close()
