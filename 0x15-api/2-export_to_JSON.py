#!/usr/bin/python3
"""Python script with a given employee ID,
returns information about his/her TODO list progress. """

from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])

    except ValueError:
        exit()
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.csv'.format(emp_id=emp_id)

    # user response
    u_res = requests.get(todo_uri).json()

    # user todo response
    t_res = requests.get(todo_uri).json()

    # all tasks
    user_tasks = list()

    for elem in t_res:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': u_res.get('username')
        }
        user_tasks.append(data)
    # create new file to save user information
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(dumps({emp_id: user_tasks}))
