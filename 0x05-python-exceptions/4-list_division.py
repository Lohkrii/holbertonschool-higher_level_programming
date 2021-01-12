#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    product_list = []
    for idx in range(list_length):
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            product = 0
            print("wrong type")
        except ZeroDivisionError:
            product = 0
            print("division by 0")
        except IndexError:
            product = 0
            print("out of range")
        finally:
            product_list.append(result)
    return product_list
