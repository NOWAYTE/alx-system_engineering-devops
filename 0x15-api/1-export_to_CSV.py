#!/usr/bin/python3
"""
Query data of an employee

"""

import csv
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    user = sys.argv[1]

    request = requests.get(url + "users/{}".format(user))
    response = request.json()

    username = response.get("username")

    params = {"userId": user}
    t_response = requests.get(url + "todos",params=params)
    todos = t_response.json()

    with open("{}.csv".format(user), mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in todos:
            writer.writerow([user, username, i.get("username"), 
                             i.get("title")])
