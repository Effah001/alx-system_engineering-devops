#!/usr/bin/python3

"""API request to reddit for subscribers"""

import requests


def number_of_subscribers(subreddit):
    user_agent = {'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; '
                  'rv: 123.0) Gecko/20100101 Firefox/123.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0
