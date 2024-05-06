#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        print(chr(ord(char) - 32), end='')
    print()
