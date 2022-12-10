#! /usr/bin/env python
"""day 8 of 2022 Advent of Code"""

import os
import pathlib
import numpy as np

def is_visible(matrix, i ,j):
    """Check if a tree is visible from outside the grid."""
    if i in [0, len(matrix)-1] or j in [0, len(matrix)-1]:
        return True
    not_vis = max(matrix[:i, j])>=matrix[i,j] and max(matrix[i+1:, j])>=matrix[i,j] and \
        max(matrix[i, :j])>=matrix[i,j] and max(matrix[i, j+1:])>=matrix[i,j]
    return not not_vis

def get_scenic_score(matrix, i, j):
    """Calculate scenic score for a specific element in the matrix"""

    visions = [matrix[i+1:, j], matrix[:i, j][::-1], matrix[i, :j][::-1], matrix[i, j+1:]]
    multipliers = np.zeros(shape=(4,), dtype=int)

    for k, vision in enumerate(visions):
        for vis in vision:
            multipliers[k] += 1
            if vis>=matrix[i,j]:
                break

    return np.prod(multipliers)

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')

with open(file_path, 'r', encoding='utf-8') as f:
    data = np.array([[int(num) for num in line] for line in  f.read().split('\n')])

result_1 = [is_visible(data, i, j) for i in range(len(data)) for j in range(len(data))]
print(sum(result_1))
result_2 = [get_scenic_score(data, i, j) for i in range(1,len(data)-1)
                                     for j in range(1,len(data)-1)]
print(max(result_2))
