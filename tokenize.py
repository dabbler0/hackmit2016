import json
import re

tweets = json.load(open('tweets.json'))

print(len(tweets))

counts = {}

tokenized_tweets = []

for tweet in tweets:
    # Strip off name and association
    tweet = tweet[tweet.index(')') + 1:]

    # Split by space
    tweet = tweet.split(' ')

    new_words = []

    for word in tweet:
        if word[:7] == 'http://' or word[:8] == 'https://':
            word = '**url**'
        elif len(word) > 0:
            if word[0] == '@':
                word = '@' + re.sub('[^a-zA-Z]', '', word[1:]).lower()
            elif word[0] == '#':
                word = '#' + re.sub('[^a-zA-Z]', '', word[1:]).lower()
            else:
                word = re.sub('[^a-zA-Z]', '', word).lower()

            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        new_words.append(word)

    tokenized_tweets.append(' '.join(new_words))

alphabet = sorted(counts, key = counts.get)
print(len(alphabet))
open('tokenized.json', 'w').write('\n'.join(tokenized_tweets))
open('alphabet.txt', 'w').write('\n'.join(alphabet))
