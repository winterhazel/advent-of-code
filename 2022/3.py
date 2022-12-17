from get_input import get_input

raw_input = get_input(3, 2022).strip()

priority_order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
rucksacks = raw_input.split('\n')

# part 1
sum_of_repeated_priorities = 0

for rucksack in rucksacks:
    first_compartment = rucksack[:len(rucksack) // 2]
    second_compartment = rucksack[len(rucksack) // 2:]
    checked_items = []

    for item in first_compartment:
        if item in checked_items:
            continue

        if item in second_compartment:
            priority = priority_order.index(item) + 1
            sum_of_repeated_priorities += priority

        checked_items.append(item)

print(sum_of_repeated_priorities)

# part 2
sum_of_badge_priorities = 0

for i in range(0, len(rucksacks), 3):
    checked_items = []

    for item in rucksacks[i]:
        if item in checked_items:
            continue

        if item in rucksacks[i + 1] and item in rucksacks[i + 2]:
            priority = priority_order.index(item) + 1
            sum_of_badge_priorities += priority
            break

        checked_items.append(item)

print(sum_of_badge_priorities)
