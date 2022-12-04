"""Day 4 of 2022 AoC"""

import os
import pathlib

def contains(tup: list[str]):
    """Check if two intervals contain each other"""
    a_0, a_1 = tup[0].split('-')
    b_0, b_1 = tup[1].split('-')
    return (int(a_0)<=int(b_0)and int(a_1)>=int(b_1)) or (int(b_0)<=int(a_0) and int(b_1)>=int(a_1))

def overlaps(tup: list[str]):
    """CHeck if two intervals overlap"""
    a_0, a_1 = tup[0].split('-')
    b_0, b_1 = tup[1].split('-')
    return int(b_0) <= int(a_0) <= int(b_1) or int(a_0) <= int(b_0) <= int(a_1)

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')


with open(file_path, 'r', encoding='utf-8') as f:
    ranges = [l.split(',') for l in f.read().split('\n')]

sol_1 = [contains(t) for t in ranges]
print(sum(sol_1))

### part 2 ###

sol_2 = [overlaps(t) for t in ranges]
print(sum(sol_2))
