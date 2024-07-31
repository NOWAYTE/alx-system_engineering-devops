#!/usr/bin/python3
"""
Query data about an employee and save it to a CSV file
"""

import csv
import json
import sys
import urllib.request

def fetch(url):
    """Fetch data from the given URL and return the JSON response."""
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data

def save(user, name, todos):
    """Save the tasks data to a CSV file."""
    filename = f"{user}.csv"
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([user, name, todo.get("completed"), todo.get("title")])

def main(user):
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{main_url}/users/{user}/todos"
    name_url = f"{main_url}/users/{user}"

    todos = fetch(todo_url)
    user_data = fetch(name_url)

    total_tasks = len(todos)
    completed_tasks = len([todo for todo in todos if todo.get("completed")])
    username = user_data.get("username")
    name = user_data.get("name")

    print(f"Employee {name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo.get("completed"):
            print(f"\t {todo.get('title')}")

    save(user, username, todos)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    main(user_id)

