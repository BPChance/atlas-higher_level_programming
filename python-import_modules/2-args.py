#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_arguments = len(argv) - 1

    if num_arguments == 0:
        print("0 arguments.", end='\n')
    elif num_arguments > 1:
        print("{} arguments:".format(num_arguments), end='\n')

        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print("{} argument:".format(num_arguments), end='\n')

        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
