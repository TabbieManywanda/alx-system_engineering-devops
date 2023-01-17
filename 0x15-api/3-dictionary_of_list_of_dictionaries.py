#!/usr/bin/python3
'''export data in the JSON format'''

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users').json()

    with open('todo_all_employees.json', 'w') as f:
        json.dump({x.get('id'): [{
            'task': y.get('title'),
            'completed': y.get('completed'),
            'username': x.get('username')}
            for y in requests.get(url + 'todos',
                                  params={'userId': x.get('id')}).json()]
            for x in users}, f)
