#!/usr/bin/python

'''
'''

from generate_log import *
from fetch_data import *
import requests

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    log = generate_log()
    print(log)
