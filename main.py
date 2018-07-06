
"""
Discord Bubble Text Generator
    Written by Elliot Potts.
    https://elliotpotts.me/


Pretty sure something like this has already been achieved, I just thought I'd try and make it using Python.
I might add a GUI later, but for now - this is a CLI.


Symbol text = :regional_indicator_THE-LETTER:
"""


import time
import pyperclip


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

string = pyperclip.paste()

newString = ""

for item in string:
    if item in alphabet:
        newString = newString + " " + ":regional_indicator_{}:".format(item)
    elif item == " ":
        newString = newString + "   "
    else:
        pass

pyperclip.copy(newString)
