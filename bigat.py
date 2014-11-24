__author__ = 'Fule Liu'

"""
百度贴吧大召唤之术。
注意：由于贴吧规则，每次召唤最多召唤5人。

TODO: 增加UI, 保存常用ID.
"""

from urllib import request
import re

from bs4 import BeautifulSoup


TEST_URL = 'http://tieba.baidu.com/p/3418442865'


def at(url, way=1):
    """召唤。
    url     target url
    way     1 means @ in horizontal, 2 means @ in vertical.
    """
    soup = BeautifulSoup(request.urlopen(url))

    users_tags = soup.find_all('a', {'alog-group': 'p_author'})
    users = [re.search(r">(.+)</a>", str(tag)).group(1) for tag in users_tags]

    users_at = ''

    # 横排@.
    if way == 1:
        for user in users:
            users_at += '@' + user + ' '
    # 竖排@.
    elif way == 2:
        for user in users:
            users_at += '@' + user + ' ' + '\n'

    return users_at


if __name__ == '__main__':
    print(at(TEST_URL, way=2))