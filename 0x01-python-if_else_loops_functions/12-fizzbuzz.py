#!/usr/bin/python3
def fidxzzbuzz():
    for idx in range(1, 101):
        if idx % 15 == 0:
            print("FizzBuzz", end=" ")
        elif idx % 5 == 0:
            print("Buzz", end=" ")
        elif idx % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{}".format(idx), end=" ")
