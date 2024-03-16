#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    return [element if i == idx else my_list[i] for i in range(len(my_list))]
