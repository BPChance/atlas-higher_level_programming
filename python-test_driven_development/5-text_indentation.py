#!/usr/bin/python3
"""defines a function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation_marks:
            lines.append(current_line.strip())
            lines.append("")  # add two new lines
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        print(line)
