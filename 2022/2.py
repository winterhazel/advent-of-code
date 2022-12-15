from ..get_input import get_input

raw_input = get_input(2, 2022).strip()

p1_shape_scores = {'X': 1, 'Y': 2, 'Z': 3}
p1_round_scores = {'AX': 3, 'BX': 0, 'CX': 6, 'AY': 6, 'BY': 3, 'CY': 0, 'AZ': 0, 'BZ': 6, 'CZ': 3}
p2_round_scores = {'X': 0, 'Y': 3, 'Z': 6}
p2_shape_scores = {'AX': 3, 'BX': 1, 'CX': 2, 'AY': 1, 'BY': 2, 'CY': 3, 'AZ': 2, 'BZ': 3, 'CZ': 1}

p1_score = p2_score = 0
for line in raw_input.split('\n'):
    enemy_shape, own_shape = line.split(' ')

    p1_score += p1_shape_scores[own_shape]
    p1_score += p1_round_scores[f'{enemy_shape}{own_shape}']

    p2_score += p2_round_scores[own_shape]
    p2_score += p2_shape_scores[f'{enemy_shape}{own_shape}']

print(p1_score, p2_score)
