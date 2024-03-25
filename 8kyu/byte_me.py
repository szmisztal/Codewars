"""If I were to ask you the size of "hello", what would you say?

Wait, let me rephrase the question:

If I were to ask you the total byte size of "hello", how many bytes do you think it takes up?

I'll give you a hint: it's not 5.

len("hello")  -->  5

byte size -->  54
54? What?!

Here's why: every string has to have an encoding (e.g ASCII),the info that makes it an object, as well as all of it's other properites... it would have to take up a bit more than 5 bytes, wouldn't it?

This might be useful for sending something over a network, where you need to represent the memory size the item takes up."""


import sys

def total_bytes(object):
    return sys.getsizeof(object)
