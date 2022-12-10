"""Solutions to the day 2 problem"""
import os
import pathlib

scores = {
    # rock       #paper     #scissors
    'A X': 1+3, 'A Y': 2+6, 'A Z': 3+0, #opp. rock
    'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6, #opp. paper
    'C X': 1+6, 'C Y': 2+0, 'C Z': 3+3, #opp. scissors
}

scores_2 = {
    # lose      #draw        #win
    'A X': 3+0, 'A Y': 1+3, 'A Z': 2+6, #opp. rock
    'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6, #opp. paper
    'C X': 2+0, 'C Y': 3+3, 'C Z': 1+6, #opp. scissors
}

file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

sol_1 = [scores[line] for line in lines]
sol_2 = [scores_2[line] for line in lines]

print(sum(sol_1))
print(sum(sol_2))
