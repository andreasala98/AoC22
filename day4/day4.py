"""Day 4 of 2022 AoC"""

import os, pathlib

def contains(t: list[str]):
    a0, a1 = t[0].split('-')
    b0, b1 = t[1].split('-')
    return (int(a0)<=int(b0) and int(a1)>=int(b1)) or (int(b0)<=int(a0) and int(b1)>=int(a1))

def overlaps(t: list[str]):
    a0, a1 = t[0].split('-')
    b0, b1 = t[1].split('-')
    return int(b0) <= int(a0) <= int(b1) or int(a0) <= int(b0) <= int(a1)

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')


with open(file_path, 'r') as f:
    ranges = [l.split(',') for l in f.read().split('\n')]


print(sum([contains(t) for t in ranges]))

### part 2 ###

print(sum([overlaps(t) for t in ranges]))