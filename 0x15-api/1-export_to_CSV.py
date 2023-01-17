#!/usr/bin/python3
'''export data in the CSV format:
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv'''

import csv
import requests
import sys


if __name__ == '__main__':
    uid = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(uid)).json()
    uname = user.get('username')
    todos = requests.get(url + 'todos', params={'userId': uid}).json()

    with open('{}.csv'.format(uid), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [uid, uname, t.get('completed'), t.get('title')])
            for t in todos]
