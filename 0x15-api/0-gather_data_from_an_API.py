#!/usr/bin/python3
"""Python script with a given employee ID,
returns information about his/her TODO list progress. """


from sys import argv
import requests

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])

    except ValueError:
        exit()
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    # response from user
    res = requests.get(user_uri).json()

    # employee name
    name = res.get('name')

    # todo response from user
    res = requests.get(todo_uri).json()

    # total number of tasks
    total = len(res)

    # No. no completed tasks
    non_completed = sum([elem['completed'] is False for elem in res])

    # No. completed
    completed = total - non_completed

    # formatting output
    str = "Employee {emp_name} is done with tasks({completed}/{total}):"

    print(str.format(emp_name=name, completed=completed, total=total))

    # completed tasks
    for elem in res:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
