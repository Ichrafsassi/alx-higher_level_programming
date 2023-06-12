#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    newlst = []

    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            newlst.append(True)
        else:
            newlst.append(False)

    return newlst
