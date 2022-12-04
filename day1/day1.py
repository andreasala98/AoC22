"""2022 Advent of Code - Day 1"""

import os
import pathlib

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data_day1.in')
print(file_path)

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

best, SCORE = 0, 0

for line in lines:
    if line!='\n':
        SCORE += int(line)
    else:
        best = max(best, SCORE)
        SCORE = 0

print(best)

### part 2 ###
print( "\n***\n")

calories = []
SCORE = 0
for line in lines:
    if line!='\n':
        SCORE += int(line)
    else:
        calories.append(SCORE)
        SCORE = 0

print(sum(sorted(calories)[::-1][:3]))
