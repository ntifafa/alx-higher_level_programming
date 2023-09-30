#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    # Get the url from the command line
    url = 'https://alx-intranet.hbtn.io/status'
    # Send the request and get the response
    response = requests.get(url)
    # Print the response
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
