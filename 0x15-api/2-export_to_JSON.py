#!/usr/bin/python3
'''Python script to export data in the JSON format:
-Records all tasks that are owned by this employee
-Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
-File name must be: USER_ID.json'''

import json
import requests
import sys


if __name__ == '__main__':
    uid = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(uid)).json()
    uname = user.get('username')
    tds = requests.get(url + 'todos', params={'userId': uid}).json()

    with open('{}.json'.format(uid), 'w') as f:
        json.dump({uid: [{
            'task': t.get('title'),
            'completed': t.get('completed'),
            'username': uname}
            for t in tds]}, f)
