"""Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False"""


from collections import Counter

def scramble(s1, s2):
    counter_s1, counter_s2 = Counter(s1), Counter(s2)
    for key in counter_s2.keys():
        if key not in counter_s1.keys() or counter_s1[key] < counter_s2[key]:
            return False
    return True




