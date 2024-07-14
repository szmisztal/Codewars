"""Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
solve("zodiacs") = 26

For the word "strength", solve("strength") = 57
-- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
For C: do not mutate input.

More examples in test cases. Good luck!"""


import re
from string import ascii_lowercase

def solve(s):
    result = []
    l = re.split("[aeiou]", s)
    for item in l:
        if len(item) > 1:
            temp_l = []
            for letter in item:
                temp_l.append(ascii_lowercase.index(letter) + 1)
            result.append(sum(temp_l))
        else:
            result.append(ascii_lowercase.index(item) + 1)
    return max(result)



print(solve("zodiacs"))
