#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for idx in my_string:
        if idx is not "c" and idx is not "C":
            new += idx
    return(new)
