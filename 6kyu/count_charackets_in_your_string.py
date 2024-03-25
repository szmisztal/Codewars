"""The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}."""


def count(s):
    if s:
        d = {}
        for i in s:
            n = s.count(i)
            d[i] = n
        return d
    else:
        return {}
