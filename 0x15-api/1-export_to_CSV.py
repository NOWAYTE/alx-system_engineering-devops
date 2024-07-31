#!/usr/bin/python3
"""
Query data about an employee

"""

import csv
import json
import sys
import urllib.request

if __name__ == "__main__":

    def fetch(url):
        with urllib.request.urlopen(url) as response:
            data = json.loads(url.read().decode())

            return data

    def save(user, name, todo):
        file = f"{user}.csv"

        with open(file, mode="w") as file:
            for i in todos:
                writer.writerow(
                        [user, name. todo.get("completed"), todo.get("title")]
                        )
