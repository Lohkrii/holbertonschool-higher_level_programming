#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for idx in names:
        if idx[:2] != "__":
            print("{}".format(idx))
