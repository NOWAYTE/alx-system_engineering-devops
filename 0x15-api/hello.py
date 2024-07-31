#!/usr/bin/python3
"""
Uses the JSON placeholder API to query data about an employee
"""
import json
import sys
import urllib.request

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    user = sys.argv[1]

    todo = f"{main_url}/users/{user}/todos"
    name_url = f"{main_url}/users/{user}"

    with urllib.request.urlopen(todo) as response:
        result = json.loads(response.read().decode())

    with urllib.request.urlopen(name_url) as response:
        n_result = json.loads(response.read().decode())

    t_num = len(result)
    complete = len([todo for todo in result if todo.get("completed")])
    name = n_result.get("name")

    print(
            "Employee {} is done with tasks({}/{}):"
            .format(name, complete, t_num)
            )
    for todo in result:
        if todo.get("completed"):
            print("\t {}".format(todo.get("title")))
