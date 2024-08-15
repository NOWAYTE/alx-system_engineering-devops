#!/usr/bin/python3
"""
Queries Reddit API and returns the number of suscribers

"""

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/".format(subreddit)

    response = requests.get(url)

    print("{}".format(response.content))


