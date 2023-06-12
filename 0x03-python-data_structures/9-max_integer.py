#!/usr/bin/python3

def max_integer(my_list=[]):
    my_list.sort()
    return None if len(my_list) == 0 else my_list[-1]
