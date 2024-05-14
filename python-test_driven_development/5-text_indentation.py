#!/usr/bin/python3
"""defines a function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation_marks:
            print(current_line.strip())
            print("")  # add two new lines
            current_line = ""

    if current_line.strip():
        print(current_line.strip(), end="")
