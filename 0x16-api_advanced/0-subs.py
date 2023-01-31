#!/usr/bin/python3
'''queries the Reddit API and returns the number of
subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given,
the function should return 0'''

import requests
import sys


def number_of_subscribers(subreddit):
    '''queries the Reddit API '''
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return 0
