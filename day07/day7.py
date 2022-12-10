"""day 7 of 2022 Advent of Code"""

import os
import pathlib

def get_size(fsys, base_path):
    """Recursively calculate size of a directory"""
    count = 0

    for obj in fsys[base_path]:
        try:
            count += int(obj)
        except ValueError:
            count += get_size(fsys, base_path + obj)

    return count

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

file_system = {'/': []}

DIR = "/"

for i in range(1, len(lines)):
    if lines[i].startswith('$ cd'):
        words = lines[i].split(' ')
        if words[2]=='..':
            DIR = '/'.join(DIR.split('/')[:-2]) + '/'
            #print(f"Switching back to {DIR}")
        else:
            DIR += words[2] + '/'

    elif lines[i] == '$ ls':
        i+=1
        try:
            while not lines[i].startswith('$'):
                words = lines[i].split(' ')
                if words[0]=='dir':
                    file_system[DIR + words[1] + '/'] = []
                    file_system[DIR].append(words[1] + '/')
                    #print(f"Adding dir {DIR + words[1] + '/'} to filesystem")
                else:
                    file_system[DIR].append(words[0])
                    #print(f"Appending {words[1]} to {DIR}")
                i+=1
        except IndexError:
            break

counts = sorted([get_size(file_system, key) for key in file_system])
size_list = [size for size in counts if size<=100000]
print(sum(size_list))

## part 2 ##

TOT_SPACE = 70000000
REQ_SPACE = 30000000

used_space = get_size(file_system, '/')
space_to_make = REQ_SPACE - TOT_SPACE + used_space

for dim in counts:
    if dim>=space_to_make:
        print(dim)
        break
