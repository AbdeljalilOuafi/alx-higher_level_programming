#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ""
    i = 0
    for char in str:
        if i == n:
            str_copy += ""
        else:
            str_copy += char
        i += 1
    return str_copy
