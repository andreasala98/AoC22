"""day 8 of 2022 Advent of Code"""

import os
import pathlib
import numpy as np

def is_visible(data, i ,j):
    """Check if a tree is visible from outside the grid."""
    if i in [0, len(data)-1] or j in [0, len(data)-1]:
        return True
    not_vis = max(data[:i, j])>=data[i,j] and max(data[i+1:, j])>=data[i,j] and \
        max(data[i, :j])>=data[i,j] and max(data[i, j+1:])>=data[i,j]
    return not not_vis

def get_scenic_score(data, i, j):
    """Calculate scenic score for a specific element in the matrix"""

    visions = [data[i+1:, j], data[:i, j][::-1], data[i, :j][::-1], data[i, j+1:]]
    multipliers = np.zeros(shape=(4,), dtype=int)

    for k, vision in enumerate(visions):
        for n in vision:
            multipliers[k] += 1
            if n>=data[i,j]:
                break
    
    return np.prod(multipliers)

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')

with open(file_path, 'r', encoding='utf-8') as f:
    data = np.array([[int(num) for num in line] for line in  f.read().split('\n')])


print(sum([is_visible(data, i, j) for i in range(len(data)) for j in range(len(data))]))
print(max([get_scenic_score(data, i, j) for i in range(1,len(data)-1) for j in range(1,len(data)-1)]))

#2211840 too high