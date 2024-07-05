#!/usr/bin/python3
"""1-hbtn_headers module"""
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as response:
    data = response.headers
    print(data["X-Request-Id"])
