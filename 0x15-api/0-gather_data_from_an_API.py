#!/usr/bin/python3
import requests
import sys

def get_employee_info(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: Unable to fetch user data for ID {employee_id}")
        return
    
    user_data = user_response.json()
    employee_name = user_data['name']
    
    # Fetch TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return
    
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)
    
    # Print the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_info(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer.")

