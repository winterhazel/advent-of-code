from math import prod

from get_input import get_input


def get_visibility(r: int, c: int):
    steps = ((0, -1), (0, 1), (-1, 0), (1, 0))
    dirs = ('left', 'right', 'top', 'bottom')

    h = int(lines[r][c])
    max_r = len(lines)
    max_c = len(lines[r])
    sides_visible_from_border = []
    sides_viewing_distance = {'left': 0, 'right': 0, 'top': 0, 'bottom': 0}

    cdir = 0
    while cdir < 4:
        cr = r
        cc = c

        visible = True
        while visible:
            cr += steps[cdir][0]
            cc += steps[cdir][1]

            if cc <= -1 or cc >= max_c or cr <= -1 or cr >= max_r:
                break
            else:
                sides_viewing_distance[dirs[cdir]] += 1
                ch = int(lines[cr][cc])
                if h <= ch:
                    visible = False
        else:
            # ended without a break (not visible)
            cdir += 1
            continue

        sides_visible_from_border.append(dirs[cdir])
        cdir += 1

    scenic_score = prod([sides_viewing_distance[direction] for direction in dirs])
    return sides_visible_from_border, scenic_score


raw_input = get_input(8, 2022).strip()
lines = raw_input.split('\n')

p1_visible_trees = 0
p1_visible_trees += len(lines) * 2  # outermost left and right trees
p1_visible_trees += (len(lines[0]) - 2) * 2  # outermost top and bottom trees
p2_highest_score = 0
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        visible_sides, score = get_visibility(i, j)

        if len(visible_sides) > 0:
            p1_visible_trees += 1

        if score > p2_highest_score:
            p2_highest_score = score

print(p1_visible_trees, p2_highest_score)
