#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return product = a / b
    except ZeroDivisionError:
        product = None
    finally:
        print("Inside result: {}".format(product))
        return product
