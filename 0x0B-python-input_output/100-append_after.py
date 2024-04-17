#!/usr/bin/python3
"""Module for append_after method"""


def append_after(filename="", search_string="", new_string=""):
    """Append a line of text to a file, after
     each line containing a specific string"""
    new_content = ""
    with open(filename, "r") as f:
        for line in f:
            new_content += line
            if search_string in line:
                new_content += new_string
    with open(filename, "w") as f:
        f.write(new_content)
