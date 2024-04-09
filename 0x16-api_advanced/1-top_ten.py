#!/usr/bin/python3

"""API request to reddit for first 10 hot post"""

import requests


def top_ten(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
                  'rv: 123.0) Gecko/20100101 Firefox/123.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        top_ten_posts = [post['data']['title'] for post in posts[:10]]
        return top_ten_posts
    else:
        print ("None")
