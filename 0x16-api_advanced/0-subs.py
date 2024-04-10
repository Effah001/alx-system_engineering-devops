#!/usr/bin/python3

"""API request to reddit for subscribers"""

import requests


def number_of_subscribers(subreddit):
    """count subreddit subscribers"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                  'rv: 123.0) Gecko/20100101 Firefox/123.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
