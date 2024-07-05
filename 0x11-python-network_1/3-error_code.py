#!/usr/bin/python3
"""error_code module"""
from urllib import request, error
from sys import argv
if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            result = response.read()
            print(result.decode("utf-8"))

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
