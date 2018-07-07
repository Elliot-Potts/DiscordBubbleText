
"""
Discord Bubble Text Generator
    Written by Elliot Potts.
    https://elliotpotts.me/


Pretty sure something like this has already been achieved, I just thought I'd try and make it using Python.
I might add a GUI later, but for now - this is a CLI program.


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
    print(r"""
  ____  _                       _   ____        _     _     _           
 |  _ \(_)___  ___ ___  _ __ __| | | __ ) _   _| |__ | |__ | | ___  ___ 
 | | | | / __|/ __/ _ \| '__/ _` | |  _ \| | | | '_ \| '_ \| |/ _ \/ __|
 | |_| | \__ \ (_| (_) | | | (_| | | |_) | |_| | |_) | |_) | |  __/\__ \
 |____/|_|___/\___\___/|_|  \__,_| |____/ \__,_|_.__/|_.__/|_|\___||___/
                                                 written by Elliot Potts                                                        
                                                                        """)
    print("""Discord Bubble Text Generator:
    - Copy the text you want to bubblify.
    - Press your hotkey
    - Paste in Discord to show bubbles.
    [!] Your hotkey can be changed at C:\Potts' Software\DiscordBubbles\settings.ini
        DEFAULT: CTRL+S+R""")


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
    string = pyperclip.paste().lower()

    print(("\n"*1) + " [+] Converting '{}' to bubble-text.".format(string))

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']

    numbers = {
        '0': ':zero:',
        '1': ':one:',
        '2': ':two:',
        '3': ':three:',
        '4': ':four:',
        '5': ':five:',
        '6': ':six:',
        '7': ':seven:',
        '8': ':eight:',
        '9': ':nine:',
        '10': ':keycap_ten:'
    }

    newString = ""

    for item in string:
        # print("ITEM = {}".format(item))
        if item in alphabet:
            newString = newString + " " + ":regional_indicator_{}:".format(item)
        elif item == "?":
            newString = newString + " " + ":question:"
        elif item == "!":
            newString = newString + " " + ":exclamation:"
        elif item in numbers.keys():
            newString = newString + " " + numbers[item]
        elif item == " ":
            newString = newString + "   "
        else:
            pass

    # print("DEBUGGING: newString = {}".format(str(newString)))
    pyperclip.copy(newString)


print(" [+] Your hotkey is {}.".format(keyToUse))

keyboard.add_hotkey(keyToUse, run)

keyboard.wait()
