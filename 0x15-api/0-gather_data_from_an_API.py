#!/usr/bin/python3
"""This Module Fetch todos of a given user.

The userId is supplied as the first argument to the script,
then the corresppomding user's todo is fetched while those completed are listed
"""
import json
from urllib import request
import sys


if __name__ == '__main__':
    url1 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        sys.argv[1])
    url2 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

    resp1 = request.urlopen(url1)
    resp2 = request.urlopen(url2)

    user = json.loads(resp2.read())
    todos = json.loads(resp1.read())

    done = (int(todo['completed']) for todo in todos)
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), sum(done), len(todos)))
    for todo in todos:
        if todo['completed']:
            print("\t{}".format(todo.get("title")))
