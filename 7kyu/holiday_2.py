"""Finding your seat on a plane is never fun, particularly for a long haul flight... You arrive, realise again just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.

To help confuse matters (although they claim in an effort to do the opposite) many airlines omit the letters 'I' and 'J' from their seat naming system.

the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the seat is (1-20 = front, 21-40 = middle, 40+ = back). This number is followed by a letter, A-K with the exclusions mentioned above.

Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.

Given a seat number, your task is to return the seat location in the following format:

'2B' would return 'Front-Left'.

If the number is over 60, or the letter is not valid, return 'No Seat!!'."""


from string import ascii_uppercase

def plane_seat(a):
    number = int(a[:-1])
    letter = a[-1]
    if number > 60 or letter in ["I", "J"] or letter not in ascii_uppercase[:11]:
        return "No Seat!!"
    if number <= 20:
        seat_n = "Front"
    elif number in range(21, 41):
        seat_n = "Middle"
    else:
        seat_n = "Back"
    if letter in ascii_uppercase[:ascii_uppercase.index("D")]:
        seat_l = "Left"
    elif letter in ascii_uppercase[ascii_uppercase.index("D"):ascii_uppercase.index("G")]:
        seat_l = "Middle"
    else:
        seat_l = "Right"
    return f"{seat_n}-{seat_l}"
