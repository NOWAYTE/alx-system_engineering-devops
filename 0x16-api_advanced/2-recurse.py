#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """A recursive function that returns a list of hot articles"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My User Agent'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")

    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
