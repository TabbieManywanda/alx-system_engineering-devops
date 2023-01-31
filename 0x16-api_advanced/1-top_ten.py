#!/usr/bin/python3
''' queries the Reddit API and prints the titles
of the first 10 hot posts listed
for a given subreddit'''

import requests
import sys


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts'''
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
