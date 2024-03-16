#!/usr/bin/env python3

from pynput.keyboard import Key, Controller
import time

clipboard = 'This will be pasted'

kb = Controller()

# Alt Tab back to previous application
with kb.pressed(Key.alt):
    time.sleep(0.5)
    kb.press(Key.tab)
    kb.release(Key.tab)

# give time for alt + tab to finish
time.sleep(0.5)

# Type each character of the clipboard one at a time
for key in clipboard:
    if key == '\n':
        kb.press(Key.enter)
        kb.release(Key.enter)
    
    elif key == '\t':
        kb.press(Key.tab)
        kb.release(Key.tab)
    
    else:
        kb.press(key)
        kb.release(key)
    
    # This is added to increase compatibility with laggy systems
    # This time can be reduced significantly with responsive systems
    # or removed completely if desired.
    # Without this line slow systems will likely not behave as expected
    time.sleep(0.05)
