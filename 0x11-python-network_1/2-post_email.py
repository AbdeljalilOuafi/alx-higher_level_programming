#!/usr/bin/python3
"""2-post_email module"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]}).encode('utf-8')
    req = request.Request(argv[1], data)

    with request.urlopen(req) as response:
        response_data = response.read()  # Read the response

    print(response_data.decode('utf-8'))
