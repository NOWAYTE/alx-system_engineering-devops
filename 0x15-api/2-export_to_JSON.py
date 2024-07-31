#!/usr/bin/python3

"""
Query data of an employee

"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = sys.argv[1]
    response = requests.get(url + "users/{}".format(user)).json()
    name = response.get("username")

    params = {"userId": user}
    todos = requests.get(url + "todos", params=params).json()

    data = {user: []}

    for i in todos:
        info = {
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": i.get("user")
                }
        data[user].append(info)

    with open("{}.json".format(user), mode="w") as file:
        json.dump(data, file, indent=4)
