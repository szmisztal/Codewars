"""Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.

Example (input -> output):
'this is a string!!' -> 'dGhpcyBpcyBhIHN0cmluZyEh'
You can learn more about Base64 encoding and decoding here.

Note: This kata uses the non-padding version ("=" is not added to the end)."""


import base64

def to_base_64(string):
    b_string = string.encode("utf-8")
    encoded = base64.b64encode(b_string)
    return encoded.decode("utf-8").rstrip("=")

def from_base_64(b64_string):
    while len(b64_string) % 4:
        b64_string += "="
    decoded = base64.b64decode(b64_string)
    return decoded.decode("utf-8")


