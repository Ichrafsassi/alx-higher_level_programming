#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    x1 = sum(map(lambda i: i[0] * i[1], my_list))
    x2 = sum(map(lambda i: i[1], my_list))

    return x1 / x2
