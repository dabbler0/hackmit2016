#retrieve user tweets was based on Craig Addyman's tutorial

from twython import Twython 
import time #standard lib
import json

CONSUMER_KEY = 'GsbVgTEQKmz4nUBaRaXGNjXSI'
CONSUMER_SECRET = 'f8aoJ96rC1aft4cnKwNq2KEAYe361wipf6we302EOpKbotPVWu'
ACCESS_KEY = '3239268835-gO55AZZzxtBgxFYaiFdOiuFvkhp8tWgO8uoeTo2'
ACCESS_SECRET = '5eZRkPsDOugawjvyoqRQXdovxqGmC97mGSwzmTyFqkXox'

def tweet_id_generator(str): #to get the lastest tweet from a user
    tw = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    tweet_ID = tw.get_user_timeline(screen_name = str, count = 1)
    return tweet_ID[0]['id'];


twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
tweets = []
for politician in json.load(open('politician-handles.json')):
    try:
        lis = [tweet_id_generator(politician)]
        for i in range(0,1):
            politician_timeline = twitter.get_user_timeline(screen_name = politician, count = 10, max_id=lis[-1])

            for tweet in politician_timeline:
                tweets.append({
                    'name': politician,
                    'tweet': tweet['text']
                })
    except:
        print 'encountered probably timeout error.'
        time.sleep(300)
        pass

    open('non-deleted-tweets.json', 'w').write(json.dumps(tweets))
