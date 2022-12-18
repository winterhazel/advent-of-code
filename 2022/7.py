import os

from get_input import get_input

raw_input = get_input(7, 2022).strip()

# map directories
directories = {}  # '/test/example': 1000
current_path = ''

for line in raw_input.split('\n'):
    if line.startswith('$'):
        # command
        command = line[2:]
        if command.startswith('cd'):
            new_folder = command[3:]
            current_path = os.path.normpath(os.path.join(current_path, new_folder))
            directories[current_path] = directories.get(current_path, 0)
        else:
            pass  # ls, do nothing
    else:
        # ls info
        if line.startswith('dir'):
            pass  # subdirs, do nothing
        else:
            # file info
            file_size, file_name = line.split(' ')
            file_size = int(file_size)
            file_path = os.path.join(current_path, file_name)
            # propagate the file size to parent directories
            reversing_path = current_path
            while reversing_path != '/':
                directories[reversing_path] = directories[reversing_path] + file_size
                reversing_path = os.path.normpath(os.path.join(reversing_path, '..'))
            directories[reversing_path] = directories[reversing_path] + file_size  # add to /

# get the answer
p1_total_sum = 0
p2_used_space = directories['/']
p2_unused_space = 70_000_000 - p2_used_space
p2_required_space = 30_000_000 - p2_unused_space
p2_chosen_directory = None

for directory in directories.keys():
    dir_size = directories[directory]

    if dir_size <= 100_000:
        p1_total_sum += dir_size

    if (p2_chosen_directory is None and p2_required_space <= dir_size) or \
            (p2_required_space <= dir_size < p2_chosen_directory[1]):
        p2_chosen_directory = (directory, dir_size)

print(p1_total_sum, p2_chosen_directory)
