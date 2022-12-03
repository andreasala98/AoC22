"""Day 3 of 2022 Advent of Code"""

import os, pathlib
from collections import Counter

def letter_score(l: str) -> int:
    return ord(l)-96 if l==l.lower() else ord(l)-64+26

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "data.in")

with open(file_path, 'r') as f:
    compartments = [(line[:len(line)//2], line[len(line)//2:]) for line in f.read().split('\n')]

print(
    sum([letter_score(list(Counter(comp[0]) & Counter(comp[1]))[0]) for comp in compartments])
)

### part 2 ###

with open(file_path, 'r') as f:
    lines = f.read().split('\n')

groups = [(lines[i], lines[i+1], lines[i+2]) for i in range(0, len(lines), 3)]

print(sum([letter_score(
            list(Counter(g[0]) & Counter(g[1]) & Counter(g[2]))[0]
        ) for g in groups]))
