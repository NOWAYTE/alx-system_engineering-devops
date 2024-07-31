#!/usr/bin/python3
"""
Uses the JSON placeholder API to query data about an employee
"""

import json
import sys
import urllib.request

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    user_id = sys.argv[1]

    todo_url = f"{main_url}/users/{user_id}/todos"
    name_url = f"{main_url}/users/{user_id}"

    # Fetch todos
    with urllib.request.urlopen(todo_url) as response:
        todos = json.loads(response.read().decode())

    # Fetch user information
    with urllib.request.urlopen(name_url) as response:
        user = json.loads(response.read().decode())

    # Calculate task information
    total_tasks = len(todos)
    completed_tasks = len([todo for todo in todos if todo.get("completed")])
    employee_name = user.get("name")

    # Print results
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo.get("completed"):
            print(f"\t {todo.get('title')}")

