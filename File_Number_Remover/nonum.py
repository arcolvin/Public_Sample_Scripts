#!/usr/bin/env python
# Created with the assistance of Bing AI
# Removes leading numbers from filenames in a given directory
# i.e. "100 file.txt" will change to "file.txt"
import os
import re

currDir = os.listdir('.')
# print(currDir)

for filename in currDir:
    if re.match(r'^[0-9]+', filename):
        new_filename = re.sub(r'^[0-9]+', '', filename)
        os.rename(filename, new_filename)
