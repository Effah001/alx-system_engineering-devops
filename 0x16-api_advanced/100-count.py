#!/usr/bin/python3
"""
Get hot titles of a subreddit
"""
import requests


def count_words(subreddit, word_list, count=None, after=""):
    """
    Recursivily get all hot title
    """
    if count is None:
        count = {}
    url = "https://www.reddit.com/r/{ subreddit}/hot.json"
    headers = {"User-Agent": "Count/1.0"}
    res = requests.get(url, headers=headers, params={"after": after})

    if res.status_code == 200:
        resq = res.json()["data"]
        after = resq["after"]
        for title in resq["children"]:
            titles = title["data"]["title"].lower().split()
            for word in word_list:
                word = word.lower()
                if word in titles:
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
        if after:
            return count_words(subred, word_list, count, after=after)
        else:
            result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

            for key, value in result:
                print(f"{key}: {value}")
            return
    else:
        return None
