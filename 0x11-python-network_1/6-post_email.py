#!/usr/bin/python3
"""
takes a URL and an email address, sends a
POST request to the passed URL with the email
as a parameter, and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    # grab the url from the command line
    url = sys.argv[1]
    # grab the email from the command line
    email = sys.argv[2]
    # store the email in a dictionary
    data = {'email': email}
    # send the request and get the response
    response = requests.post(url, data=data)
    # print the response body
    print("{}".format(response.text))
