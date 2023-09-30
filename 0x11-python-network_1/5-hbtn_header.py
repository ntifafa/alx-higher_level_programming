#!/usr/bin/python3
"""
takes a URL, sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    # grab the url from the command line
    url = sys.argv[1]
    # send the request and get the response
    response = requests.get(url)
    # print the X-Request-Id header
    print("{}".format(response.headers.get('X-Request-Id')))
