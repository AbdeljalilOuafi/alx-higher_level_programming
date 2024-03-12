#!/usr/bin/python3
def uppercase(str):
    string = ""
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            string += chr(ord(char) - 32)
        else:
            string += char
    print("{:s}".format(string))
