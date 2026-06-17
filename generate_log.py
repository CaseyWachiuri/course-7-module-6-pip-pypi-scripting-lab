#!/usr/bin/python

'''
'''

from datetime import datetime

def generate_log(log_data):
    # Validation (It must be worthy!? The chosen one!!!!!
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    # file name value
    filename = f"log_{datetime.now().strftime("%Y%m%d")}.txt"

    # write to file
    with open(filename, "w") as file:
        for item in log_data:
            file.write(str(item) + "\n")

    # Print out confirmation
    print(f'Log written to {filename}')

    # Return the filename
    return file

