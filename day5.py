"""day 5 solution - 2022 Advent of Code"""

import os
import pathlib

def read_char(block):
    candidate = block[1]
    return candidate if candidate!=' ' else ''

def initialize_stacks(input_text):
    lines = input_text.split('\n')
    lgth = len(lines[0])
    stacks = [[] for _ in range(lgth)]

    for line in lines[:-1]:
        cursor = 0
        k = 0
        while cursor<len(line):
            stacks[k].append(read_char(line[cursor:cursor+4]))
            cursor+=4
            k+=1
    stacks = [[stk for stk in stack if stk!=''][::-1] for stack in stacks if stack!=[]]
    return stacks

def set_command_list(command_list):
    return [(word.split(' ')[1], word.split(' ')[3], word.split(' ')[5]) for word in command_list.split('\n')]

def process_commands(stacks, commands):
    for quant, dep, dest in commands:
        
        mover = stacks[dep].pop()
        stacks[dest].extend([mover])


file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')

with open(file_path, 'r', encoding='utf-8') as f:
    chunks = f.read().split('\n\n')

cranes = chunks[0]
commands = chunks[1]

stacks = initialize_stacks(cranes)
commands = set_command_list(commands)

process_commands(stacks, commands)
