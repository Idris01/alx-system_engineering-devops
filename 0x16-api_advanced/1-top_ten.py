#!/usr/bin/python3
"""Prints title of top ten posts of a given reddit
"""

import requests
import sys


def top_ten(subreddit):
    """Prints title of top ten posts of a subreddit
    """
    url_template = 'https://www.reddit.com/r/{}/top.json?limit=10'

    try:
        resp = requests.get(
                url_template.format(subreddit),
                headers={'User-Agent': 'idrisoft'},
                allow_redirects=False)
        data = resp.json()
        for post in data['data']['children']:
            print(post['data'].get('title'))
    except Exception as e:
        print('None')


if __name__ == '__main__':
    top_ten(sys.argv[1])
