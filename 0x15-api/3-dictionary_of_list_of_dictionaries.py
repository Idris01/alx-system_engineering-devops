#!/usr/bin/python3
"""Exports todo list of all users to json
"""
import json
import sys
from urllib import request


if __name__ == '__main__':
    file_name = "todo_all_employees.json"
    all_data = {}
    for user_id in range(1, 11):
        url1 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                user_id)
        url2 = "https://jsonplaceholder.typicode.com/users/{}".format(
            user_id)

        resp1 = request.urlopen(url1)
        resp2 = request.urlopen(url2)

        user = json.loads(resp2.read())
        todos = json.loads(resp1.read())
        data = (dict(
                    task=todo.get("title"),
                    completed=todo.get("completed"),
                    username=user.get("username")) for todo in todos)

        all_data["{}".format(user.get("id"))] = list(data)
    with open(file_name, 'w') as stream:
        stream.write(json.dumps(all_data))
