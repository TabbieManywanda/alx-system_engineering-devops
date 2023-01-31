#!/usr/bin/python3
'''Recursive function that queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
'''

import requests
import sys


def add_title(hot_list, hot_posts):
    '''add items'''
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    '''You may change the prototype,
    but it must be able to be called with just a subreddit
    If not a valid subreddit, return None.'''
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code != 200:
        return None

    dic = response.json()
    hot_posts = dic['data']['children']
    add_title(hot_list, hot_posts)
    after = dic['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
