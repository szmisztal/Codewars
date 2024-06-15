"""Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: https://leetcode.com/problems/two-sum/"""


from itertools import combinations

def two_sum(numbers, target):
    comb = combinations(numbers, 2)
    for i in comb:
        if sum(i) == target:
            if i[0] == i[1]:
                temp_list = numbers.copy()
                temp_list[temp_list.index(i[0])] = "0"
                return (numbers.index(i[0]), temp_list.index(i[1]))
            return (numbers.index(i[0]), numbers.index(i[1]))



