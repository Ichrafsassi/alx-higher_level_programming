#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list : prints elements from this list
        x : number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    n = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (n)
