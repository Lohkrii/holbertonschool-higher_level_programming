#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for idx in my_string:
        if my_string[idx] is not "c" and my_string[idx] is not "C":
            new += idx
    return(new)
