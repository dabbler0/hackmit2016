import urllib
from urllib import request
import html
import re
import json

p = re.compile('\\/user\\/[^\\/]*\\/')

result = []

for i in range(1, 39):
    response = urllib.request.urlopen('http://politwoops.sunlightfoundation.com/users?page=%d&per_page=50' % i)
    result += p.findall(str(response.read()))
    print('Finished %d / 39' % i)

f = open('politician-handles.json', 'w')
f.write(json.dumps(list(map(lambda x: x.split('/', 3)[2], result))))
