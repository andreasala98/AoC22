"""day 11 of 2022 Advent of Code"""

import os
import pathlib
import re
import math

def print_monkeys(monkey_li):
    """Visualize monkey situtation"""
    for i,monk in enumerate(monkey_li):
        print(f"Monkey {i}: {monk.items}")

    print()
    for i,monk in enumerate(monkey_li):
        print(f"Monkey {i}: {monk.count}")

class Monkey:
    """A funny yet naughty animal"""
    def __init__(self, desc: str) -> None:
        lines = desc.split('\n')
        self.items = [int(item) for item in re.findall(r'\d+', lines[1])]

        self.op_dc = lines[2].split(' ')[-2:]

        self.test = lambda x: x%int(lines[3].split()[-1])==0
        self.div = int(lines[3].split()[-1])
        self.throw_true = int(lines[4].split(' ')[-1])
        self.throw_false = int(lines[5].split(' ')[-1])

        self.count = 0

    def set_worry_level(self, item:int) -> int:
        """Calculate worry level."""
        if self.op_dc[0]=='*':
            wor_lev = item**2 if self.op_dc[1]=='old' else item*int(self.op_dc[1])
        elif self.op_dc[0]=='+':
            wor_lev =  item*2 if self.op_dc[1]=='old' else item+int(self.op_dc[1])
        else:
            raise ValueError
        return wor_lev #% self.div

    def inspect(self, monkey_list: list, lcm):
        """Inspect objects"""
        while self.items:
            item = int(self.items.pop(0))

            worry_level = self.set_worry_level(int(item)) % lcm

            if self.test(worry_level):
                monkey_list[self.throw_true].insert_item(worry_level)
            else:
                monkey_list[self.throw_false].insert_item(worry_level)

            self.count += 1

    def insert_item(self, new_item):
        """Receive a new item"""
        self.items.append(new_item)


file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data.in')

with open(file_path, 'r', encoding='utf-8') as f:
    monkey_desc = f.read().split('\n\n')

monkeys = [Monkey(descr) for descr in monkey_desc]

LCM = math.lcm(*[mo.div for mo in monkeys])

for _ in range(10000):
    for monkey in monkeys:

        monkey.inspect(monkeys, LCM)

monkey_counts = [mon.count for mon in monkeys]
monkey_business = sorted(monkey_counts)[-2] * sorted(monkey_counts)[-1]

print_monkeys(monkeys)
print(monkey_business)
