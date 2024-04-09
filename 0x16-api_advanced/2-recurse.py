#!/usr/bin/python3
"""API request to reddit for hot articles for a given subreddit"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch all posts from a subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return hot_list

    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                  'rv: 123.0) Gecko/20100101 Firefox/123.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=user_agent, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data'])
        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
    else:
        return None
