from get_input import get_input

raw_input = get_input(4, 2022).strip()

p1_contained_pairs = p2_overlaps = 0

for pair in raw_input.split('\n'):
    first_elf, second_elf = pair.split(',')

    f_start, f_end = first_elf.split('-')
    f_range = set(range(int(f_start), int(f_end) + 1))
    s_start, s_end = second_elf.split('-')
    s_range = set(range(int(s_start), int(s_end) + 1))

    intersection = f_range.intersection(s_range)
    if len(intersection) > 0:
        p2_overlaps += 1
        if len(intersection) == len(f_range) or len(intersection) == len(s_range):
            p1_contained_pairs += 1

print(p1_contained_pairs, p2_overlaps)
