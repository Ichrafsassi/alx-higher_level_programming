#!/usr/bin/python3
for x1 in range(0, 10):
    for x2 in range(x1 + 1, 10):
        if x1 == 8 and x2 == 9:
            print("{}{}".format(x1, x2))
        else:
            print("{}{}".format(x1, x2), end=", ")
