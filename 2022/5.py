from get_input import get_input
import re

raw_input = get_input(5, 2022).strip()

crate_arrengement, instructions = raw_input.split('\n\n')

# get starting arrengement
lines = crate_arrengement.split('\n')
col_count = int(lines.pop()[-2])
crates = [''] * col_count

for line in lines[-1::-1]:
    for col, item in enumerate(line[1::4]):
        if item != ' ':
            crates[col] += item

# move crates
p1_crates = crates.copy()
p2_crates = crates.copy()

for instruction in instructions.split('\n'):
    search = re.search('move (.*) from (.*) to (.*)', instruction)
    quantity, origin, dest = [int(x) for x in search.group(1, 2, 3)]

    p1_moved_crates = p1_crates[origin - 1][-1:-quantity - 1:-1]
    p1_crates[origin - 1] = p1_crates[origin - 1][:len(p1_crates[origin - 1]) - quantity:1]
    p1_crates[dest - 1] += p1_moved_crates

    p2_moved_crates = p2_crates[origin - 1][len(p2_crates[origin - 1]) - quantity:]
    p2_crates[origin - 1] = p2_crates[origin - 1][:len(p2_crates[origin - 1]) - quantity]
    p2_crates[dest - 1] += p2_moved_crates

print(p1_crates, p2_crates)
