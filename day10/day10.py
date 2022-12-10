"""day 10 of 2022 Advent of Code"""

import os
import pathlib

def draw(drawing_, cycle_, x_c):
    cycle_ = cycle_ % 40
    if cycle_%40==0:
        drawing_ += '\n'
    if x_c-1 <= cycle_ <= x_c+1:
        drawing_ += '#'
    else:
        drawing_ += ' '
    return drawing_

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

cycles_to_check = [20,60,100,140,180, 220]

cycle = 1
tot = 1
result = 0


for line in lines:
    cmd = line.split(' ')
    if cycle in cycles_to_check:
        result += cycle*tot
    if cmd[0]=='noop':
        cycle+=1
    else:
        cycle+=1
        if cycle in cycles_to_check:
            result += cycle * tot
        cycle += 1
        tot += int(cmd[1])

print(result)

### part 2 ###

CYCLE = -1
x = 1
DRAWING= ''
for line in lines:
    cmd = line.split(' ')

    if cmd[0]=='noop':
        CYCLE+=1
        DRAWING = draw(DRAWING, CYCLE, x)
    else:
        CYCLE +=1
        DRAWING = draw(DRAWING, CYCLE, x)
        CYCLE+=1
        DRAWING = draw(DRAWING, CYCLE, x)
        x += int(cmd[1])

print(DRAWING)
