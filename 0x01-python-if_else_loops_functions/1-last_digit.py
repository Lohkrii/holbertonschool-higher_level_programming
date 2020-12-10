#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_num = number % 10
elif number < 0:
    last_num = number % -10

r_str = "Last digit of {:d} is "
if last_num > 5:
    print("{:s}{:d} and is greater\
        than 5".format(number, last_num))
elif last_num == 0:
    print("{:s}{:d} and is 0".format(number, last_num))
else:
    print("{:s}{:d} and is less than 6 and not 0"
        .format(number, last_num))
