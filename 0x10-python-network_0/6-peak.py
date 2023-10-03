#!/usr/bin/python3
"""Find peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """list of unsorted integers"""
    list_of_integers = sorted(list_of_integers)
    return list_of_integers[-1]
