#!/usr/bin/python3
"""
    Find a peak at unsorted list of integers
"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    size = len(list_of_integers)

    peak = list_of_integers[size - 1]

    list_int = list_of_integers

    for i in range(0, size - 1, 1):

        if 0 < i < size - 1:
            if list_int[i - 1] < list_int[i] > list_int[i + 1]:
                peak = list_int[i]
    return peak