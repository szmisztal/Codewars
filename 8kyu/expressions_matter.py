"""Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained (Read the notes for more detail about it)
Example
With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
So the maximum value that you can obtain is 9."""


def expression_matter(a, b, c):
    e_1 = a * (b + c)
    e_2 = a * b * c
    e_3 = a + b * c
    e_4 = (a + b) * c
    return max(e_1, e_2, e_3, e_4)


