#!/usr/bin/python3
"""queries the Reddit API and return the
number of total subscribers """

import requests
def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/subscribers.json'.format(subreddit)
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16 task 0)'}
    response = requests.get(url, headers=headers)
    if (not response.ok):
        return 0
    subscriber_count = response.json().get('data').get('subscribers')
    return subscriber_count
