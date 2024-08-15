#!/usr/bin/python3
"""
Queries Reddit API and returns the number of suscribers

"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-Agent':  'My User Agent 1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        return data.get('data').get('subscribers')
    else:
        return 0

if __name__ == "__main__":
    main()
