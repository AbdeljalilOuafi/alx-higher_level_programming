#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list.

    Args:
        my_list (list): list of all elements.
        x (int):  number of time you need to go over the list
    Return:
        number of elements printed.
    """
    iter = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            iter += 1
        except IndexError:
            break
    print()
    return iter
