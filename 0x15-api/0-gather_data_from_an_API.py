#!/usr/bin/python3
"""using rest api"""
import requests as r
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    do = r.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    completed = [title.get("title") for title in to_do if
            title.get('completed') is True]
    print(completed)
    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                             len(completed),
                                                             len(to_do)))
    [print("\t {}".format(title)) for title in completed]
