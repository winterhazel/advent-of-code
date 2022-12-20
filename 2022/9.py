from get_input import get_input

raw_input = get_input(9, 2022).strip()

DIRECTION_MOVES = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
ROPE_SIZE = 10

r_pos = [[0, 0] for i in range(ROPE_SIZE)]
tail_positions = set()
tail_positions.add(f'{r_pos[ROPE_SIZE - 1]}')

for line in raw_input.split('\n'):
    direction, steps = line.split(' ')

    for i in range(int(steps)):
        for k_idx, knot in enumerate(r_pos):
            # move the head
            if k_idx == 0:
                r_pos[0][0] += DIRECTION_MOVES[direction][0]
                r_pos[0][1] += DIRECTION_MOVES[direction][1]
                continue

            # move the knots
            pk_pos = r_pos[k_idx - 1]
            k_pos = r_pos[k_idx]
            diff = (pk_pos[0] - k_pos[0], pk_pos[1] - k_pos[1])
            k_dist = (diff[0] ** 2 + diff[1] ** 2) ** 1 / 2
            if k_dist > 1:
                movement = [0, 0]
                if diff[0] != 0:
                    # needs to move horizontally
                    movement[0] = 1 if pk_pos[0] > k_pos[0] else -1
                if diff[1] != 0:
                    # needs to move vertically
                    movement[1] = 1 if pk_pos[1] > k_pos[1] else -1

                r_pos[k_idx][0] += movement[0]
                r_pos[k_idx][1] += movement[1]

                if k_idx == ROPE_SIZE - 1:
                    tail_positions.add(f'{r_pos[k_idx]}')

print(len(tail_positions))
