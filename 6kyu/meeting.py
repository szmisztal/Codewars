"""John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
It can happen that in two distinct families with the same family name two people have the same first name too.

Notes
You can see another examples in the "Sample tests"."""


def meeting(s):
    sep_list = list(i.split(":") for i in s.upper().split(";"))
    temp_dict = {i[1]: [] for i in sep_list}
    temp_dict = dict(sorted(temp_dict.items()))
    for i in sep_list:
        temp_dict[i[1]].append(i[0])
        temp_dict[i[1]].sort()
    result = []
    for key, value in temp_dict.items():
        for sub_item in value:
            result.append(f"({key}, {sub_item})")
    return "".join(result)

