#!/usr/bin/env python3

import requests
import json

# Get Octocat ASCII Art
octocat = requests.get('https://api.github.com/octocat')

# Get Rate information
rate = requests.get('https://api.github.com/rate_limit')
limits = json.loads(rate.text)

# Extract rate information from the created JSON Dictionary
remaining = limits['resources']['core']['remaining']
limit = limits['resources']['core']['limit']

print(octocat.text)

print('Remaining Core Resources:')
print(f'Total Request limit per hour: {limit}')
print(f'Calls remaining this hour: {remaining}\n')
