#!/usr/bin/python3
""" module doc """


def find_peak(list_of_integers):
    """def doc"""
    if list_of_integers:
        left = 0
        right = len(list_of_integers) - 1
        while left < right:
            middle = (left + right) // 2
            if list_of_integers[middle] > list_of_integers[middle + 1]:
                right = middle
            else:
                left = middle + 1
        return list_of_integers[left]
