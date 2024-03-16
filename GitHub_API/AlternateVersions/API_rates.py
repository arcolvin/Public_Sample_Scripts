#!/usr/bin/env python3

import requests
import json
import datetime

def authenticate(cfgFile):
    with open(cfgFile) as tokenFile:
        user = tokenFile.readline().strip('\n')
        token = tokenFile.readline().strip('\n')
    return requests.auth.HTTPBasicAuth(user, token)

def rateCheck(token=None):
    if token != None:
        rate = requests.get('https://api.github.com/rate_limit', auth=token)
    else:
        rate = requests.get('https://api.github.com/rate_limit')

    
    limits = json.loads(rate.text)

    remaining = limits['resources']['core']['remaining']
    limit = limits['resources']['core']['limit']
    used = limits['resources']['core']['used']
    reset = datetime.datetime.fromtimestamp(limits['resources']['core']['reset'])

    print('Remaining Core Resources:')
    print(f'Total Request limit per hour: {limit}')
    print(f'Calls remaining this hour: {remaining}')
    print(f'Used Resources: {used}')
    print(f'Reset Time: {reset} (Local Time)\n\n')

if __name__ == '__main__':

    user = 'ADD_USERNAME_HERE' # Modify string to your username
    token = 'ADD_TOKEN_HERE' # Modify String to contain your token

    basicAuth = requests.auth.HTTPBasicAuth(user, token)

    print('Unauthenticated Rates:')
    rateCheck()

    print('Authenticated Rates:')
    rateCheck(basicAuth)