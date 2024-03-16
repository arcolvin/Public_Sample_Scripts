#!/usr/bin/env python3

import urllib.parse
import requests
import json
import datetime

url = 'https://api.github.com/octocat'
params = ''
speak = input("What should Octocat say? (blank for random): ")
finStr = ''

user = 'ADD_USERNAME_HERE' # Modify string to your username
token = 'ADD_TOKEN_HERE' # Modify String to contain your token

basicAuth = requests.auth.HTTPBasicAuth(user, token)

if speak:
    for let in speak:
        # Filter out characters which might make the request break
        if let.lower() in 'abcdefghijklmnopqrstuvwxyz0123456789 ':
            finStr += let
    # Create a URL compatible string from the user's input
    params = f"?{urllib.parse.urlencode({'s': finStr})}"


octocat = requests.get(url + params, auth=basicAuth)

rate = requests.get('https://api.github.com/rate_limit', auth=basicAuth)
limits = json.loads(rate.text)

# Extract data from JSON
remaining = limits['resources']['core']['remaining']
limit = limits['resources']['core']['limit']
used = limits['resources']['core']['used']
reset = datetime.datetime.fromtimestamp(limits['resources']['core']['reset'])

print(octocat.text)

print('Remaining Core Resources:')
print(f'Total Request limit per hour: {limit}')
print(f'Calls remaining this hour: {remaining}')
print(f'Used Resources: {used}')
print(f'Reset Time: {reset} (Local Time)\n')
