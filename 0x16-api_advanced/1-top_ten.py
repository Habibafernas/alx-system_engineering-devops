#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": 'Google Chrome Version 81.0.4044.129'
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params)
    results = response.json()
    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
