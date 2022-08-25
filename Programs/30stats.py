#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

nums = []
for i in range(len(sys.argv) - 1):
	nums.append(float(sys.argv[i+1]))
nums.sort()

# Mean
num_sum = sum(nums)
mean = num_sum/len(nums)

# Standard Deviation
numerator = 0
for i in range(len(nums)):
	numerator += ((nums[i] - mean) ** 2)
std_dev = math.sqrt((numerator)/(len(nums)))

# Median
if (len(nums) % 2 != 0): 
	median = nums[int(len(nums)/2)]
else:
	median = nums[int(len(nums)/2)] + nums[int((len(nums)/2)) + 1] / 2

# Print Results
print(f'Count: {len(nums)}')
print(f'Minimum: {nums[0]:.1f}')
print(f'Maximum: {nums[len(nums)-1]:.1f}')
print(f'Mean: {mean:.3f}')
print(f'Std. dev: {std_dev:.3f}')
print(f'Median: {median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
