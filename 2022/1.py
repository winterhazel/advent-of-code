from ..get_input import get_input

raw_input = get_input(1, 2022).strip()

bag = [x for x in raw_input.split('\n\n')]
total = []

for elf in bag:
    elf_sum = sum(int(x) for x in elf.split('\n'))
    total.append(elf_sum)
total.sort()

print(total[-1])
print(total[-1] + total[-2] + total[-3])
