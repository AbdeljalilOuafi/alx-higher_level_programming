#!/usr/bin/python3
"""Module for read_file"""


def read_file(file=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(file, encoding="utf-8") as f:
        print(f.read(), end="")
