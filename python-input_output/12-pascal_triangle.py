#!/usr/bin/python3
"""define a module"""


def pascal_triangle(n):
    """define a function"""
    if n <= 0:
        return
    
    triangle = [[1]]

    for i in range(1, i):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)
    # print the triangle
    for row in triangle:
        print(row)
