#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    r_d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    sums = 0
    for current, next_num in zip(roman_string, roman_string[1:]):
        if r_d[current] >= r_d[next_num]:
            sums += r_d[current]
        else:
            sums -= r_d[current]

    sums += r_d[roman_string[-1]]
    return sums
