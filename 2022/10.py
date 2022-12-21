from get_input import get_input

raw_input = get_input(10, 2022).strip()

MAX_CYCLE = 240
COMMAND_STEPS = {'noop': 1, 'addx': 2}

commands = raw_input.split('\n')
cmd_queue = []
cycle = 1
x = 1

p1_strength_sum = 0

while True:
    # strength
    if (cycle - 20) % 40 == 0:
        p1_strength_sum += cycle * x

    # draw the screen
    cx = (cycle - 1) % 40
    if cx == 0:
        print()
    if cx in (x - 1, x, x + 1):
        print('█', end='')
    else:
        print('.', end='')

    # add command to queue
    if cycle <= len(commands):
        cmd_queue.append([*commands[cycle - 1].split(), 0])

    # execute current command
    if len(cmd_queue) > 0:
        c_cmd = cmd_queue[0]
        c_cmd[-1] += 1  # increment command step
        if c_cmd[-1] >= COMMAND_STEPS[c_cmd[0]]:
            cmd_queue.pop(0)
            if c_cmd[0] == 'addx':
                x += int(c_cmd[1])

    cycle += 1
    if cycle > MAX_CYCLE:
        break

print(f'\n{p1_strength_sum}')
