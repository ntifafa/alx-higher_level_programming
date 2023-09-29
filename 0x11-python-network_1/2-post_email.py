#!/usr/bin/python3
"""
takes a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request



if __name__ == "__main__":
    # get the url from the command line
    url = sys.argv[1]
    # get the email from the command line
    email = sys.argv[2]
    # encode the email
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    # send the request
    with urllib.request.urlopen(url, data) as response:
        content = response.read().decode('utf-8')
        print("{}".format(content))
