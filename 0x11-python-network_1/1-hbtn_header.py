#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id"""
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as response:
    data = response.headers
    print(data["X-Request-Id"])
