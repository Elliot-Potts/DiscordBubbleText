
"""
Discord Bubble Text Generator
    Written by Elliot Potts.
    https://elliotpotts.me/


Pretty sure something like this has already been achieved, I just thought I'd try and make it using Python.
I might add a GUI later, but for now - this is a CLI.


Symbol text = :regional_indicator_THE-LETTER:
"""


import time
import keyboard
import pyperclip
import configparser
import os

projPath = "C:\Potts' Software\DiscordBubbles"
configp = configparser.ConfigParser()
keyToUse = None


def runOnStart():
    print("""Discord Bubble Text Generator:
    - Copy the text you want to bubblify.
    - Press your hotkey (C:\Potts' Software\DiscordBubbles\settings.ini
    - Paste in Discord to show bubbles.
    [!] Your hotkey can be changed, and is default to CTRL+S+R""")


runOnStart()


def settingsInit():
    if os.path.isdir(projPath):
        os.chdir(projPath)

        if os.path.isfile("settings.ini"):
            confO = configp.read("settings.ini")
            global keyToUse
            keyToUse = configp.get("main", "hotkey")
        else:
            getHotKey = "ctrl+s+r"
            makeConf = open("settings.ini", "w")
            configp.add_section("main")
            configp.set("main", "hotkey", getHotKey)
            configp.write(makeConf)
            makeConf.close()

            settingsInit()
    else:
        os.makedirs(projPath)
        settingsInit()


settingsInit()


def run():
    string = pyperclip.paste()

    print(("\n"*3) + " [+] Converting {} to bubble-text.".format(string))

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']

    newString = ""

    for item in string:
        if item in alphabet:
            newString = newString + " " + ":regional_indicator_{}:".format(item)
        elif item == " ":
            newString = newString + "   "
        else:
            pass

    pyperclip.copy(newString)


print(" [+] Your hotkey is {}.".format(keyToUse))

keyboard.add_hotkey(keyToUse, run)

keyboard.wait()
