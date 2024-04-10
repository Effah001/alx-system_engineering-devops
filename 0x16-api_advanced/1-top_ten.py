#!/usr/bin/python3

"""API request to reddit for first 10 hot post"""

import requests


def top_ten(subreddit):
    """Get the top 10 posts"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': "TopHotPost/1.0 {by Wills}"}
    url = f"https://www.reddit.com/r/{subreddit}/top.json"
    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        top_ten_posts = [post['data']['title'] for post in posts[:10]]
        return top_ten_posts
    else:
        print("None")
