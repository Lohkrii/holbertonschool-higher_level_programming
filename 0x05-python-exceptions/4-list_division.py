#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_product_list = []
    for idx in range(list_length):
        product = 0
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("Wrong type")
        except ZeroDivisionError:
            print("Division by 0")
        except IndexError:
            print("out of range")
        finally:
            my_product_list.append(result)
    return my_product_list
