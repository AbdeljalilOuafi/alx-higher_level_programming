#!/usr/bin/python3
"""8-hbtn_header module"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    param = {"q": q}
    response = requests.post(url, data=param)
    try:
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(response_json["id"], response_json["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
