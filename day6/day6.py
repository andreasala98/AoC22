"""day 6 of 2022 Advent of Code."""

import os
import pathlib

def solve(word, num):
    """Solve day6 part1 and part2"""
    start = 0
    while len(set(word[start:start+num]))<num:
        start+=1
    return start + num

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')

with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read()

print(solve(data, 4))
print(solve(data, 14))
