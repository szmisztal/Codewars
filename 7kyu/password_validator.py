"""Your job is to create a simple password validation function, as seen on many websites.

The rules for a valid password are as follows:

There needs to be at least 1 uppercase letter.
There needs to be at least 1 lowercase letter.
There needs to be at least 1 number.
The password needs to be at least 8 characters long.
You are permitted to use any methods to validate the password.

Examples:
password("Abcd1234"); ===> true
password("Abcd123"); ===> false
password("abcd1234"); ===> false
password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"); ===> true
password("ABCD1234"); ===> false
password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"); ===> true;
password("!@#$%^&*()-_+={}[]|\:;?/>.<,"); ===> false;
Extra info
You will only be passed strings.
The string can contain any standard keyboard character.
Accepted strings can be any length, as long as they are 8 characters or more."""


def password(string):
    if len(string) < 8:
        return False
    d = {"upper": False, "lower": False, "number": False}
    for i in string:
        if i.isupper():
            d["upper"] = True
        elif i.islower():
            d["lower"] = True
        elif i.isdigit():
            d["number"] = True
    if all(d.values()) == True:
        return True
    return False

