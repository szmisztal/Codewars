"""A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation."""


from string import ascii_lowercase

def is_pangram(s):
    s = s.lower()
    for char in ascii_lowercase:
        if char not in s:
            return False
    return True


