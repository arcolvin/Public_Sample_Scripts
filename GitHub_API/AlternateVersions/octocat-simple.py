#!/usr/bin/env python3

import requests

octocat = requests.get('https://api.github.com/octocat')

print(octocat.text)
