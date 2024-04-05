"""Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of [1, 26]."""


from string import ascii_uppercase

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = ascii_uppercase + ascii_uppercase

    def encode(self, st):
        result_str = ""
        for i in st.upper():
            index = self.alphabet.find(i)
            new_index = index + self.shift
            if i in self.alphabet:
                result_str += self.alphabet[new_index]
            else:
                result_str += i
        return result_str.upper()

    def decode(self, st):
        result_str = ""
        for i in st.upper():
            index = self.alphabet.find(i, 25)
            new_index = index - self.shift
            if i in self.alphabet:
                result_str += self.alphabet[new_index]
            else:
                result_str += i
        return result_str.upper()
