"""ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating."""


from string import ascii_lowercase, ascii_uppercase

def rot13(message):
    upper_alph = ascii_uppercase + ascii_uppercase
    lower_alph = ascii_lowercase + ascii_lowercase
    result = ""
    for i in message:
        if i.islower():
            result += lower_alph[lower_alph.index(i) + 13]
        elif i.isupper():
            result += upper_alph[upper_alph.index(i) + 13]
        else:
            result += i
    return result

