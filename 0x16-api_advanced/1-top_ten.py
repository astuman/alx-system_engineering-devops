#!/usr/bin/python3
"""A function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """print the titles of the first 10 hot posts
    listed for a given subreddit."""
    base_url = 'https://api.reddit.com'
    api_url = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)
    # set User-Agent
    user_agent = {'User-Agent': 'Python/requests'}
    load = {'limit': '10'}
    # Get response
    r = requests.get(api_url, headers=user_agent,
                     params=load, allow_redirects=False)
    # check validity of subreddit
    if r.status_code in (302, 404):
        print('None')
    else:
        # print the titles of the first 10 hot posts
        res_json = r.json()

        if res_json.get('data') and res_json.get('data').get('children'):
            hot_posts = res_json.get('data').get('children')
            for post in hot_posts:
                if post.get('data') and post.get('data').get('title'):
                    print(post.get('data').get('title'))
