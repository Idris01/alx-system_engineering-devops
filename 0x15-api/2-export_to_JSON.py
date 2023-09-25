#!/usr/bin/python3
"""Exports todo list of a given user to json
"""
import json
import sys
from urllib import request


if __name__ == '__main__':
    url1 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        sys.argv[1])
    url2 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

    resp1 = request.urlopen(url1)
    resp2 = request.urlopen(url2)

    user = json.loads(resp2.read())
    todos = json.loads(resp1.read())
    with open("{}.json".format(sys.argv[1]), 'w') as stream:
        data = (dict(
                    task=todo.get("title"),
                    completed=todo.get("completed"),
                    username=user.get("username")) for todo in todos)

        stream.write(json.dumps({
            "{}".format(user.get("id")): list(data)}))
