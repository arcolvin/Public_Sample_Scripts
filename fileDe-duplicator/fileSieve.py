#!/usr/bin/env python3

import os
import shutil

'''
App will compare filenames from location one and two. Any duplicate names will
be moved from LOCATION_1 to the MV_LOCATION. These potentially duplicate files
can then be reviewed and manually deleted at the user's digression.
'''

###################################
# Start Environment Configuration #
###################################

# Set to true to actually move files
# Set to false to see matches and size of matched lists
active = False

# Are these files on the local file system (True) or Network Share files (False)
# TODO: This might not be needed. Simply set to remote for all attempts for
#   better compatibility
LOCAL = True

# Comparison Locations (Files will be removed from Location 1)
LOCATION_1 = "/home/example/pictures"
LOCATION_2 = "/home/example2/pictures"
# Where files will be relocated to for review
MV_LOCATION = "/tmp/possibleDups"

#################################
# End Environment Configuration #
#################################

# Obtain file listing from location 2
os.chdir(LOCATION_2)
DIR_2 = os.listdir()

# Obtain file listing from location 1
os.chdir(LOCATION_1)
DIR_1 = os.listdir()

# Function to verify provided X is a file, not a directory
filterFunc = lambda x: os.path.isfile(x)

# Eliminate any directories from file lists
filtered_1 = list(filter(filterFunc, DIR_1))
filtered_2 = list(filter(filterFunc, DIR_2))

matches = set(filtered_1) & set(filtered_2)

if active:
    # Create output DIR if not already exist
    if not os.path.exists(MV_LOCATION):
        os.makedirs(MV_LOCATION)

    for i, file in enumerate(matches):
        print(f'Moving {i+1} of {len(matches)}')
        
        if LOCAL:
            # Use if all files are on the same File System
            os.rename(file, f'{MV_LOCATION}/{file}')

        else:
            # Use if files are on different File systems (Like a NAS)
            shutil.move(file, f'{MV_LOCATION}/{file}')

else:
    print('Matches:', matches)
    print(f'Filter 1 Len: {len(filtered_1)}')
    print(f'Filter 2 Len: {len(filtered_2)}')
    print(f' Matched Len: {len(matches)}')
