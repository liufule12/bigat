__author__ = 'Fule Liu'

from urllib import request
from bs4 import BeautifulSoup
import re


webpage = request.urlopen('http://tieba.baidu.com/p/3418442865')
soup = BeautifulSoup(webpage)

lis = soup.find_all('li', {'class': 'd_name'})

users_tags = soup.find_all('a', {'alog-group': 'p_author'})

users = [re.search(r">(.+)</a>", str(tag)).group(1) for tag in users_tags]

users_at = ''

for user in users:
    users_at += '@' + user + ' '

print(users_at)