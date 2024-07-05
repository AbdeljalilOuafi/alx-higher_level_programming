#!/usr/bin/python3

from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    data = response.read()

print("Body response:\n\t\
- type: {}\n\t\
- content: {}\n\t- utf8 content: {}".format(
    type(data), data, data.decode('utf8')))
