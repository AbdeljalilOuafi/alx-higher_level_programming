#!/usr/bin/python3
from urllib import request
from sys import argv
url = argv[1]
with request.urlopen(url) as response:
    data = response.headers
    print(data["X-Request-Id"])
