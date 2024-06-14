"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""


def pig_it(text):
    l = []
    for i in text.split(" "):
        if not i.isalpha():
            l.append(i)
        else:
            p = i[1:]
            p += i[0] + "ay"
            l.append(p)
    return " ".join(l)

