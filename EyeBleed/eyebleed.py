#!/usr/bin/env python3
import sys
import random

'''
This program will take input text and output that same text with random letter sizes
and fonts which will likely be borderline unreadable!

Why? Cause why not! Also more practice with text / file manipulation
'''

if len(sys.argv) < 2:
    print("Provide input file name.")
    exit()

inputFile = sys.argv[1]

# Open plaintext file and save to string
# add option to select input file with sys.argv?
with open(inputFile, 'r') as f:
    # print(f.read())
    rawText = f.read()

# Build base HTML Headers
htmlHead= '''<!DOCTYPE html>
<html>
<head>
<title>
I'm So Sorry
</title>
<style>
</style>
<head>
<body>
'''

htmlBody = ''

htmlTail = '''</body>
</html>'''

# Create code to parse input text and assign random or sequential modifications
# assign random values to letter paramaters
# sz -> Font Size
sz = lambda: str(random.randint(10,100))

# col -> Font Color
col = lambda: str(hex(random.randint(0,255)))[2:].zfill(2)

# wt -> Font Weight (Bold?)
wt = lambda: random.choice(range(100, 1000, 100))

# st -> Font Style (Italic?)
st = lambda: random.choice(('normal', 'italic','oblique'))

# fnt -> Font Family
fnt = lambda: random.choice(('cursive', 'serif', 'sans-serif'))

for x in rawText:
    if x == '\n':
        htmlBody += '<br>\n'
    else:
        htmlBody += f'<span style="font-size:{sz()}px; color:#{col()}{col()}{col()}; font-weight:{wt()}; font-style:{st()}; font-family:{fnt()};">{x}</span>\n' 


# build the final html string and write to file
with open('out.html', 'w') as f:
    f.write(htmlHead + htmlBody + htmlTail)


