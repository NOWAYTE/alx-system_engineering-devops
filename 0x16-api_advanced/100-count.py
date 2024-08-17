#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the
titles of all articles and prints the sorted count of given keywords.

"""

import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """ Recursive function to count keywords in hot articles """

    if word_count is None:
        word_count = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {
        "after": after,
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
    titles = data.get("children")

    word_list = [word.lower() for word in word_list]

    for title in titles:
        t = title.get("data").get("title").lower()
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + t.count(word)

    if after is not None:
        return count_words(subreddit, word_list, after, word_count)

    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_word_count:
        if count > 0:
            print(f"{word}: {count}")

    return word_count
