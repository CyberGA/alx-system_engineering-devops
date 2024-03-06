#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(f'http://www.reddit.com/r/{subreddit}/about.json',
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by cyberga)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
