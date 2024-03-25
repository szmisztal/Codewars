"""Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]"""


def tower_builder(n_floors):
    l = []
    for i in range(1, n_floors * 2, 2):
        l.append("*" * i)

    new_l = []
    j = n_floors - 1
    for s in l:
        new_l.append(" " * j + s + " " * j)
        j -= 1
    return new_l
