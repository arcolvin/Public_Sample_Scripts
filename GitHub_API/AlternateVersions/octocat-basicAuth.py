#!/usr/bin/env python3

import requests
import json

user = 'ADD_USERNAME_HERE' # Modify string to your username
token = 'ADD_TOKEN_HERE' # Modify String to contain your token

basicAuth = requests.auth.HTTPBasicAuth(user, token)


octocat = requests.get('https://api.github.com/octocat', auth=basicAuth)

rate = requests.get('https://api.github.com/rate_limit', auth=basicAuth)
limits = json.loads(rate.text)

# Extract data from JSON
remaining = limits['resources']['core']['remaining']
limit = limits['resources']['core']['limit']

print(octocat.text)

print('Remaining Core Resources:')
print(f'Total Request limit per hour: {limit}')
print(f'Calls remaining this hour: {remaining}\n')
