#!/usr/bin/python

'''
'''

from datetime import datetime
import requests

def generate_log():
    log_data = []
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return f"Log written to {filename}"
