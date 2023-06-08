#!/usr/bin/python3
import sys


def add_args(argv):
    total = 0
    for arg in argv:
        total += int(arg)
    return total


if __name__ == "__main__":
    output = add_args(sys.argv[1:])
    print(output)
