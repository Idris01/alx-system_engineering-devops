#!/usr/bin/python3
"""Fetch todos of a given user
"""
import urllib.request as request
import json
import sys

url1 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        sys.argv[1])
url2 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

if __name__ == '__main__':
    resp1 = request.urlopen(url1)
    resp2 = request.urlopen(url2)

    user = json.loads(resp2.read())
    todos = json.loads(resp1.read())
    with open("{}.csv".format(sys.argv[1]), 'w') as stream:
        for todo in todos:
            data = '"{}","{}","{}","{}"\n'.format(
                    user.get("id"),
                    user.get("username"),
                    todo.get("completed"),
                    todo.get("title"))
            stream.write(data)
