#!/usr/bin/python

'''
'''

import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()

    return {}
