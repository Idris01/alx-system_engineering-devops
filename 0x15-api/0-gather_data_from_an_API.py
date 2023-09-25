#!/usr/bin/python3
"""This Module Fetch todos of a given user from an API
and then print a formated output of the
completed todos while also showing the proprtion of the completed tasks
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

    done = (int(todo['completed']) for todo in todos)
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), sum(done), len(todos)))
    for todo in todos:
        if todo['completed']:
            print("\t{}".format(todo.get("title")))
