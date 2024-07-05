#!/usr/bin/python3
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        data = response.read().decode('utf-8')

print("Body response:\n\t\
- type: {}\n\t\
- content: {}".format(
    type(data), data))
