"""given a matrix n x n (2-7), determine if the arrow is directed to the target (x).
Now there are one of 4 types of arrows ( '^', '>', 'v', '<' ) and only one target (x)
An empty spot will be denoted by a space " ", the target with a cross "x", and the scope ">"
Examples:
given matrix 4x4:
[
  [' ', 'x', ' ', ' '],
  [' ', ' ', ' ', ' '], --> return true
  [' ', '^', ' ', ' '],
  [' ', ' ', ' ', ' ']
]
given matrix 4x4:
[
  [' ', ' ', ' ', ' '],
  [' ', 'v', ' ', ' '], --> return false
  [' ', ' ', ' ', 'x'],
  [' ', ' ', ' ', ' ']
]
given matrix 4x4:
[
  [' ', ' ', ' ', ' '],
  ['>', ' ', ' ', 'x'], --> return true
  [' ', '', ' ', ' '],
  [' ', ' ', ' ', ' ']
]

In this example, only a 4x4 matrix was used, the problem will have matrices of dimensions from 2 to 7"""


def solution(mtrx):
    for l in mtrx:
        for item in l:
            if item == "x":
                list_index = mtrx.index(l)
                target_index = l.index(item)
    if ">" in mtrx[list_index][:target_index] or "<" in mtrx[list_index][target_index:]:
        return True
    for l in mtrx:
        if "v" in l[target_index] and l in mtrx[:list_index] or "^" in l[target_index] and l in mtrx[list_index:]:
            return True
    return False
