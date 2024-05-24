#!/usr/bin/python3
"""exports to CSV"""

from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv


if __name__ == "__main__":
    main = "https://jsonplaceholder.typicode.com"
    todo = main + "/user/{}/todos".format(argv[1])
    name = main + "/users/{}".format(argv[1])
    t_result = get(todo).json()
    n_result = get(name).json()

    t_list = []
    for todo in t_result:
        t_dict = {}
        t_dict.update({"user_ID": argv[1], "username": n_result.get(
            "username"), "completed": todo.get("completed"),
                          "task": todo.get("title")})
        t_list.append(t_dict)
    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        head = ["user_ID", "username", "completed", "task"]
        write = DictWriter(f, fieldnames=head, quoting=QUOTE_ALL)
        write.writerows(t_list)
    with open("{}.json".format(argv[1]), 'w') as f:
                dump({argv[1]: t_list}, f)

