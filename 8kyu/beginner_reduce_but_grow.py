"""Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24"""


def grow(arr):
    i = arr[0]
    for j in arr[1:]:
        i *= j
    return i
