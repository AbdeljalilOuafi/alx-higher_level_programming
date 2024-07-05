#!/usr/bin/python3
"""4-hbtn_status"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t\
    - type: {}\n\t\
    - content: {}\n\t".format(
        type(response), response.text))
