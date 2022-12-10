"""day 9 of 2022 Advent of Code"""

import os
import pathlib
import copy

def dist(point_1, point_2):
    """Distance with funny metric"""
    return max(abs(point_1[0]-point_2[0]), abs(point_1[1] - point_2[1]))

def move_head(dir_, head_):
    """Move head"""

    if dir_=='R':
        head_[0]+=1
    elif dir_=='L':
        head_[0]-=1
    elif dir_=='U':
        head_[1]+=1
    else:
        head_[1]-=1
    return head_

def move_tail(head_, prev_head_, tail_, visit, i_x):
    """Move tail if it is too far from the head"""
    #print(f"Distance: {dist(head_, tail_)}")
    if dist(head_, tail_)<=1:
        #print("Tail does not move")
        pass
    else:
        #HT are stretched, move tail closer
        tail_ [0], tail_[1] = prev_head_[0], prev_head_[1]
        if (tail_[0],tail_[1]) not in visit:
            visit.add((tail_[0], tail_[1]))
            if i_x==9:
                print(f"Added {(tail_[0], tail_[1])} to knot {i_x}")

    return tail_, visit


file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.test')

with open(file_path, 'r', encoding='utf-8') as f:
    commands = f.read().split('\n')


head = [0,0]
tail = [0,0]
prev_head = ['a','a']
visited = set((0,0))

# for cmd in commands:
#     dir, quant = cmd.split(' ')

#     for _ in range(int(quant)):

#         prev_head[0] = head[0]
#         prev_head[1] = head[1]
#         head = move_head(dir, head)
#         #print(f"Head moves to {head}. Tail at {tail}. Prev head {prev_head}")
#         tail, visited = move_tail(head, prev_head, tail, visited)
#         #print(f"Head at {head}. Tail moved at {tail}.")
#         #print()


# visited.add((0,0))
# print(len(visited)-1)

## part 2 ##

visited_2 = [set() for _ in range(10)]
for j in range(10):
    visited_2[j].add((0,0))
knots = [[0,0] for _ in range(10)]

for cmd in commands:
    dire, quant = cmd.split(' ')

    for _ in range(int(quant)):
        prev_knots = copy.deepcopy(knots)
        knots[0] = move_head(dire, knots[0])

        for j in range(1, 10):
            knots[j], visited_2[j] = move_tail(
                head_=knots[j-1],
                prev_head_=prev_knots[j-1],
                tail_=knots[j],
                visit=visited_2[j],
                i_x=j
            )

print(len(visited_2[9])-1)
