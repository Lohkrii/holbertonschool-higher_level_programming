#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return(None)
    max_int = my_list[0]
    for idx in my_list:
        if idx > max_int:
            max_int = idx
    return(max_int)
