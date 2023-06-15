#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    n = 0
    for i in uniq_list:
        n += i

    return (n)
