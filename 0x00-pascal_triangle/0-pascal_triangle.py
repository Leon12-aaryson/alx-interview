#!/usr/bin/python3
""" Returns a representation of a Pascal's triangle """


def pascal_triangle(n):
    """ Returns a list of lists for Pascal's triangle"""
    pascal_list = []
    for row in range(n):
        if row == 0:
            pascal_list.append([1])
        else:
            previous_row = pascal_list[-1]
            new_row = [1] + [previous_row[i] + previous_row[i + 1]
                            for i in range(len(previous_row) - 1)] + [1]
            pascal_list.append(new_row)
    return pascal_list