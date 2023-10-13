#!/usr/bin/python3
"""Define functions that interract with the reddit api
"""


from collections import defaultdict
import requests
import sys


def count_words(
        subreddit,
        word_list,
        after=None,
        word_map=defaultdict(lambda: 0)):
    """Recursively print the number of word in a given subreddit
    """
    url_template = 'https://www.reddit.com/r/{}/hot.json{}'
    new_after = ""

    try:
        url = url_template.format(
                subreddit,
                "" if after is None else (
                    "?after=" + after))
        resp = requests.get(
                url,
                headers={'User-Agent': 'idrisoft'},
                allow_redirects=False)
        if resp.status_code > 299:
            raise Exception('redirect occur')
        data = resp.json()
        new_after = data['data']['after']

        for post in data['data']['children']:
            title = post['data']['title'].lower().split()
            found = []
            for word in word_list:
                found_word = word.lower()
                if found_word not in found:
                    found.append(found_word)
                    wc = title.count(found_word)
                    if wc:
                        word_map[found_word] += wc
    except Exception as e:
        return

    if new_after is not None:
        count_words(subreddit, word_list, new_after, word_map)
        return
    word_map = dict(word_map)
    for key in sorted(list(word_map.keys())):
        print("{}: {}".format(key, word_map[key]))


if __name__ == '__main__':
    count_words(sys.argv[1], sys.argv[2].split())
