"""Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:

choose a text in capital letters including or not digits and non alphabetic characters,

shift each letter by a given number but the transformed letter must be a letter (circular shift),
replace each digit by its complement to 9,
keep such as non alphabetic and non digit characters,
downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
reverse the whole result.
Example:
your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"

With longer passphrases it's better to have a small and easy program. Would you write it?"""


from string import ascii_lowercase

def play_pass(s, n):
    result = ""
    l = []
    for index, value in enumerate(list(s)):
        if value.isalpha():
            l.append((ascii_lowercase * 2)[ascii_lowercase.find(value.lower()) + n])
        elif value.isdigit():
            l.append(str(9 - int(value)))
        else:
            l.append(value)
    for index, value in enumerate(l):
        if value.isalpha():
            if index % 2 == 0:
                result += value.upper()
            else:
                result += value.lower()
        else:
            result += value
    return result[::-1]


print(play_pass("BORN IN 2015!", 1))
