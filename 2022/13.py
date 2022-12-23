from get_input import get_input
import ast

raw_input = get_input(13, 2022).strip()


def compare_pair(left: list, right: list) -> bool:
    for a, b in zip(left, right):
        if isinstance(a, int) and isinstance(b, int):
            if a != b:
                return a < b
        else:
            r = compare_pair([a] if isinstance(a, int) else list(a), [b] if isinstance(b, int) else list(b))
            if r is not None:
                return r

    if len(left) != len(right):
        return len(left) < len(right)


# part 1
pairs = raw_input.split('\n\n')
packets = []
p1_idx_sum = 0
for idx, pair in enumerate(pairs):
    a, b = pair.split('\n')
    left = ast.literal_eval(a)
    right = ast.literal_eval(b)
    if compare_pair(left, right):
        p1_idx_sum += idx + 1

    packets.append(left)  # for part 2
    packets.append(right)

print(p1_idx_sum)

# part 2
idx_2 = 1
idx_6 = 2
for packet in packets:
    if compare_pair(packet, [[2]]):
        idx_2 += 1
    if compare_pair(packet, [[6]]):
        idx_6 += 1

print(idx_2 * idx_6)
