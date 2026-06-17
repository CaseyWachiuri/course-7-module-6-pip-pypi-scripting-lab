#!/usr/bin/python

'''
'''

import os
import sys
import pytest
from datetime import datetime

from generate_log import *
from fetch_data import *

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    log = generate_log()
    print(log)
