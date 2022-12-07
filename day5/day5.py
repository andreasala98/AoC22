"""day 5 solution - 2022 Advent of Code"""

import os
import pathlib
import copy

def read_char(block):
    """Read charachter from one of the stacks."""
    candidate = block[1]
    return candidate if candidate!=' ' else ''

def initialize_stacks(input_text):
    """Read the initial configuration of stacks."""
    lines = input_text.split('\n')
    lgth = len(lines[0])
    starting_stacks = [[] for _ in range(lgth)]

    for line in lines[:-1]:
        cursor = 0
        k = 0
        while cursor<len(line):
            starting_stacks[k].append(read_char(line[cursor:cursor+4]))
            cursor+=4
            k+=1
    staks = [[stk for stk in stack if stk!=''][::-1] for stack in starting_stacks if stack!=[]]
    return staks

def set_command_list(cmd_list):
    """Parse useful numbers from the list of commands"""
    return [(word.split(' ')[1], word.split(' ')[3], word.split(' ')[5]
                ) for word in cmd_list.split('\n')]

def process_commands_9000(stacks, commands):
    """Process and apply the moving commands for CrateMover9000."""
    for quant, dep, dest in commands:
        for _ in range(int(quant)):
            mover = stacks[int(dep)-1].pop()
            stacks[int(dest)-1].append(mover)

    return stacks

def process_commands_9001(stacks, commands):
    """Process and apply the moving commands for CrateMover9001."""
    for quant, dep, dest in commands:

        movers = stacks[int(dep)-1][-int(quant):]
        del stacks[int(dep)-1][-int(quant):]

        stacks[int(dest)-1].extend(movers)

    return stacks

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')

with open(file_path, 'r', encoding='utf-8') as f:
    chunks = f.read().split('\n\n')

cranes = chunks[0]
command_list = chunks[1]

stacks1 = initialize_stacks(cranes)
stacks2 = copy.deepcopy(stacks1)
cmnds = set_command_list(command_list)

stacks_9000 = process_commands_9000(stacks1, cmnds)
stacks_9001 = process_commands_9001(stacks2, cmnds)

print(''.join([stk[-1] for stk in stacks_9000]))
print(''.join([stk[-1] for stk in stacks_9001]))
