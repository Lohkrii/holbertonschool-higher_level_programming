#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    product = []
    for idx in my_list:
        if idx % 2 == 0:
            product.append(True)
        else:
            product.append(False)
    return(product)
