from get_input import get_input

raw_input = get_input(12, 2022).strip()

ELEVATIONS = 'abcdefghijklmnopqrstuvwxyz'
MOVES = ((1, 0), (-1, 0), (0, 1), (0, -1))


def get_height(char: str) -> int:
    return ELEVATIONS.index(char)


def get_possible_moves(x: int, y: int) -> list[list[int]]:
    possible_moves = []
    h = get_height(lines[y][x])
    for move in MOVES:
        cx = x + move[0]
        cy = y + move[1]
        if -1 in (cx, cy) or cx >= len(lines[0]) or cy >= len(lines):
            continue
        if get_height(lines[cy][cx]) - h <= 1:
            possible_moves.append([cx, cy])
    return possible_moves


def bfs(start, end):
    explored_positions = {tuple(start): 0}  # (x, y): steps
    queue = [(start, 0)]
    while len(queue) > 0:
        pos, steps = queue.pop(0)
        if pos == end:
            break
        steps += 1
        for n_pos in get_possible_moves(pos[0], pos[1]):
            if tuple(n_pos) not in explored_positions.keys() or explored_positions[tuple(n_pos)] > steps:
                explored_positions[tuple(n_pos)] = steps
                queue.append((n_pos, steps))
    return explored_positions.get(tuple(end), float('inf'))


lines = raw_input.split('\n')

# find S and E
start = [-1, -1]
end = [-1, -1]
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            start = [x, y]
            lines[y] = lines[y].replace('S', 'a')
        elif char == 'E':
            end = [x, y]
            lines[y] = lines[y].replace('E', 'z')
        if -1 not in (*start, *end):
            break

# part 1
p1_path_length = bfs(start, end)
print(p1_path_length)

# part 2
p2_shortest_path_length = p1_path_length
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == 'a':
            p2_shortest_path_length = min(p2_shortest_path_length, bfs([x, y], end))
print(p2_shortest_path_length)
