"""2022 Advent of Code - Day 1"""

import os
import pathlib

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data_day1.in')
print(file_path)

with open(file_path, 'r') as f:
    lines = f.readlines()

best, actual = 0, 0

for line in lines:
    if line!='\n':
        actual += int(line)
    else:
        best = max(best, actual)
        actual = 0

print(best)

### part 2 ###
print( "\n***\n")

calories = []
actual = 0
for line in lines:
    if line!='\n':
        actual += int(line)
    else:
        calories.append(actual)
        actual = 0

print(sum(sorted(calories)[::-1][:3]))




