import time

import pyperclip

last_one = ""

def get_next():
    global last_one
    while True:
        this_one = pyperclip.paste()
        if this_one != last_one:
            time.sleep(1000)
        else:
            last_one = this_one
            return this_one
