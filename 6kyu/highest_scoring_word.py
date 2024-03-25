"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""


from string import ascii_lowercase

def high(x):
    l = x.split()
    word_dict = {}
    letter_value = 0
    for word in l:
        for letter in word:
            letter_value += ascii_lowercase.index(letter) + 1
        word_dict[word] = letter_value
        letter_value = 0
    temp_value = 0
    for key, value in word_dict.items():
        if value <= temp_value:
            pass
        else:
            result_key, temp_value = key, value
    return result_key


