#!/usr/bin/python3
for idx in range(0, 10):
    for cidx in range(idx + 1, 10):
        print("{:d}{:d}".format(idx, cidx), end ="")
        if idx * 10 + cidx != 89:
            print(", ", end="")
print("")
