#!/usr/bin/python3
"""
queries data about an employee
"""

from requests import get
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    todo = url + "/user/{}/todos".format(argv[1])
    name = url + "/users/{}".format(argv[1])
    t_result = get(todo).json()
    n_result = get(name).json()


    t_num = len(t_result)
    t_complete = len([todo for todo in t_result
                         if todo.get("completed")])
    name = n_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, t_complete, t_num))
    for todo in t_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
