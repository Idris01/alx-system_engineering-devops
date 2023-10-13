#!/usr/bin/python3
"""Prints title of top ten posts of a given reddit
"""

import requests
import sys


def recurse(subreddit, after=None):
    """Prints title of top ten posts of a subreddit
    """
    url_template = 'https://www.reddit.com/r/{}/hot.json{}'
    titles = []
    new_after = None

    try:
        url = url_template.format(
                subreddit,
                "" if after is None else (
                    "?after=" + after))
        print(url)
        resp = requests.get(
                url,
                headers={'User-Agent': 'idrisoft'},
                allow_redirects=False)
        data = resp.json()
        new_after = data['data']['after']
        titles.extend(list(
            post['data']['title'] for post in
            data['data']['children']))
    except Exception as e:
        return 'None'

    if new_after is not None:
        titles.extend(recurse(subreddit, new_after))
        return titles

    return titles


if __name__ == '__main__':
    print(recurse(sys.argv[1]))
