"""When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"""


from string import ascii_lowercase

def position(alphabet):
    return f"Position of alphabet: {ascii_lowercase.index(alphabet.lower()) + 1}"
