"""Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered."""


def increment_string(strng):
    if not strng or not strng[-1].isdigit():
        return strng + "1"
    s = strng.rstrip("".join(str(i) for i in range(10)))
    tail_s = strng[len(s):]
    tail = int(tail_s) + 1
    result = s + str(tail).zfill(len(tail_s))
    return result


