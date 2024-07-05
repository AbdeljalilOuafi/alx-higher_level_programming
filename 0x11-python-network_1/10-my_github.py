#!/usr/bin/python3
"""10-my_github"""
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    headers = {'Authorization': f'Bearer {password}'}
    response = requests.get("https://api.github.com/user", headers=headers)
    if (response.status_code >= 400):
        print("None")
        exit()
    print(response.json()["id"])
