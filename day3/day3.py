"""Day 3 of 2022 Advent of Code"""

import os
import pathlib
from collections import Counter

def letter_score(letter: str) -> int:
    """Assign integer score to each letter"""
    return ord(letter)-96 if letter.islower() else ord(letter)-64+26

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "data.in")

with open(file_path, 'r', encoding='utf-8') as f:
    compartments = [(line[:len(line)//2], line[len(line)//2:]) for line in f.read().split('\n')]

sol_1 = [letter_score(list(Counter(comp[0]) & Counter(comp[1]))[0]) for comp in compartments]
print(sum(sol_1))

### part 2 ###

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

groups = [(lines[i], lines[i+1], lines[i+2]) for i in range(0, len(lines), 3)]

sol_2 = [letter_score(
            list(Counter(g[0]) & Counter(g[1]) & Counter(g[2]))[0])
         for g in groups]

print(sum(sol_2))
