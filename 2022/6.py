from get_input import get_input


def find_sequence_with_distinct_characters(raw_input: str, num_of_chars: int):
    for i in range(len(raw_input[num_of_chars:])):
        sequence = raw_input[i:i + num_of_chars]
        distinct_chars = set(sequence)
        if len(distinct_chars) == num_of_chars:
            print(i + num_of_chars)
            break


raw_input = get_input(6, 2022).strip()
find_sequence_with_distinct_characters(raw_input, 4)
find_sequence_with_distinct_characters(raw_input, 14)
