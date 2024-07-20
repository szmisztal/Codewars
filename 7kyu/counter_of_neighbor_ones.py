"""Task
Tranform of input array of zeros and ones to array in which counts number of continuous ones. If there is none, return an empty array

Example
[1, 1, 1, 0, 1] -> [3,1]
[1, 1, 1, 1, 1] -> [5]
[0, 0, 0, 0, 0] -> []"""


def ones_counter(inp):
    result, count = [], 0
    for i in inp:
        if i == 1:
            count += 1
        else:
            if count != 0:
                result.append(count)
            count = 0
    if count != 0:
        result.append(count)
    return result

