#!/usr/bin/python3
# Prime generator performance testing template
import time

#################################################
## Add initialized Variables or functions here ##
#################################################

# start the timer
start = time.time_ns() # Gives sub second accuracy

######################################
## Add Algorithm to Test Below Here ##
######################################



######################################
## Add Algorithm to Test Above Here ##
######################################

# stop the timer
end = time.time_ns()

# Calculate number of seconds
elapsed = (end - start) / 1e9

# Show the time required to complete algorithm
print(f'{elapsed} seconds elapsed')

###################################################
## Perform Any Final un-timed Actions Below Here ##
###################################################
