"""You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]"""


def sort_array(source_array):
    final_list = []
    even_list = []
    copy_list = source_array.copy()
    for i in source_array:
        if i % 2 != 0:
            final_list.append(i)
        else:
            even_list.append((copy_list.index(i), i))
            copy_list.remove(i)
            copy_list.insert(source_array.index(i), "a")
    final_list.sort()
    for i in even_list:
        final_list.insert(i[0], i[1])
    return final_list

