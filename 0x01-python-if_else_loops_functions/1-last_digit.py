#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ndigit = abs(number) % 10
if number < 0:
    ndigit = -ndigit
print("Last digit of {} is {} and is ".format(number, ndigit), end="")
if ndigit > 5:
    print("greater than 5")
elif ndigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
