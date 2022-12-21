from math import prod

from get_input import get_input

raw_input = get_input(11, 2022).strip()

lines = raw_input.split('\n')
lines.append('\n')

monkeys = []

cm_idx = 0
cm_dict = {}
for line in lines:
    if len(line) == 0 or line == lines[-1]:
        monkeys.append(cm_dict.copy())
        continue

    match (line.strip().split(':')):
        case ['Starting items', items]:
            i_list = [int(item) for item in items.strip().replace(' ', '').split(',')]
            cm_dict['items'] = i_list
        case ['Operation', op]:
            op_items = op.strip().split()
            op_a = op_items[2]
            op_b = op_items[-1]
            fn = sum if op_items[-2] == '+' else prod
            operation = (fn, op_a, op_b)
            cm_dict['operation'] = operation
        case ['Test', test]:
            num = int(test.strip().split()[-1])
            cm_dict['d_num'] = num
        case ['If true', op]:
            dest = int(op.strip().split()[-1])
            cm_dict['dt_dest'] = dest
        case ['If false', op]:
            dest = int(op.strip().split()[-1])
            cm_dict['df_dest'] = dest
        case _:
            # new monkey
            cm_idx = int(''.join([c for c in line.strip() if c.isnumeric()]))

ROUNDS = 10000
cr = 0
monkey_inspections = [0 for monkey in monkeys]
lcm = prod([monkey['d_num'] for monkey in monkeys])

while cr < ROUNDS:
    cr += 1
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            monkey_inspections[monkeys.index(monkey)] += 1
            item = monkey['items'][0] % lcm
            # inspect
            operands = []
            for operand in monkey['operation'][1:3]:
                operands.append(item if operand == 'old' else int(operand))
            i_result = monkey['operation'][0](operands)  # // 3
            # throw the item
            dest = 'dt_dest' if (i_result % monkey['d_num']) == 0 else 'df_dest'
            monkeys[monkey[dest]]['items'].append(i_result)
            monkey['items'].pop(0)

monkey_inspections.sort()
print(monkey_inspections[-1] * monkey_inspections[-2])
