#!/usr/bin/python3
"""
Get the subscribers count of a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
    Subreddit subscribers count
    """
    # Check if subreddit is None or not a string
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MySubs/1.0"}  # Custom User-Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Check if the 'subscribers' key exists in the response data
        if 'subscribers' in data['data']:
            return data['data']['subscribers']
    return 0  # Return 0 for invalid subreddit or if subscribers count is not available
