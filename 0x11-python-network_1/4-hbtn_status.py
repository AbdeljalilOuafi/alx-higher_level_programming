#!/usr/bin/python3
"""4-hbtn_status"""
import requests


response = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:\n\t\
- type: {}\n\t\
- content: {}".format(
    type(response.text), response.text))
