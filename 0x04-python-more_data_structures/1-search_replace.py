#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = list(map(lambda x: replace if x == search else x, my_list))
    return (newList)
