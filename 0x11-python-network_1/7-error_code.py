#!/usr/bin/python3
"""
sends a request to a given URL and displays the response body.
"""
import sys
import requests


if __name__ == "__main__":
    # grab URL from the command line arguments
    url = sys.argv[1]

    # send an HTTP GET request to the specified URL
    r = requests.get(url)
    # check if the response status code is greater than or equal to 400
    if r.status_code >= 400:
        # print an error message with the HTTP status code
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
