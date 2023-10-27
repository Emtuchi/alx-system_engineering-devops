#!/usr/bin/python3
"""using rest api"""
import requests as r
import sys
import json

if __name__ == '__main__':
    name_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    employee_id = sys.argv[1]
    params = {"id" : employee_id}
    params2 = {"userId" : employee_id}

    user = r.get(name_url, params).json()
    tasks = r.get(todo_url, params2).json()

    name = ""
    for user_dict in user:
        name = user_dict.get('name')

    tasks_num = 0
    done_task = 0
    for task in tasks:
        tasks_num += 1

        if task['completed']:
            done_task += 1

    print("Employee {} is done with tasks ({}/{}):".format
            (name, done_task, tasks_num))

    for title in tasks:
        if title['completed']:
            print("\t"+title['title'])
