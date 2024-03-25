"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F"""


def abbrev_name(name):
    lst = name.split(" ")
    f_name = lst[0][0] + "."
    s_name = lst[1][0]
    return f_name.upper() + s_name.upper()
