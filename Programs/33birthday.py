#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Give them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random
import sys

number_people = int(sys.argv[1])
number_trials = int(sys.argv[2])
shared_bdays = 0

# do multiple trials

for i in range (number_trials):
	# start with empty calendar and counter each trial
	calendar = [0] * 365
	
	# store birthday for each person
	for person in range(number_people):
		birthday = random.randint(0,364)
		calendar[birthday] += 1
	
	# check for shared birthday (shared if greater than 1)
	for i in range (len(calendar)):
		if (calendar[i] > 1):
			shared_bdays += 1
			
# report results
prob_shared = shared_bdays/ (number_trials)
print(f'Probability of {number_people} sharing a birthday is {prob_shared:.3f}')

"""
python3 33birthday.py
0.571
"""

