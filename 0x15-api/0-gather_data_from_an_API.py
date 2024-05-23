#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    m_url = 'https://jsonplaceholder.typicode.com'
    t_url = m_url + "/user/{}/todos".format(argv[1])
    n_url = m_url + "/users/{}".format(argv[1])
    t_result = get(t_url).json()
    n_result = get(n_url).json()

    t_num = len(t_result)
    t_complete = len([todo for todo in t_result
                         if todo.get("completed")])
    name = n_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, t_complete, t`_num))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
