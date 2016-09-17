from lxml import html
import requests
import re
import json

all_tweets = []

for i in range(1, 495):
    page = requests.get('http://politwoops.sunlightfoundation.com/?page=%d&per_page=50' % i)
    tree = html.fromstring(page.content)

    tweets = list(filter(
        lambda x: x != ' ',
        map(lambda x: re.sub('\s+', ' ', x.text_content()), tree.xpath('//div[@class="tweet-content"]'))
    ))

    print('Completed %d / 494' % i)

    all_tweets += tweets

    k = open('tweets.json', 'w')
    k.write(json.dumps(all_tweets))
    k.close()
