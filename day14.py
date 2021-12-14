from helper.input import read_input
import sys
from collections import defaultdict


def create_state(input):
    [[template]] = read_input(14, input + '_1', [(str,)])
    state = defaultdict(int)
    for i in range(len(template) - 1):
        state[template[i] + template[i + 1]] += 1

    first_char = template[0]
    last_char = template[-1]

    return state, first_char, last_char


def create_mapping_table(input):
    mapping_table = dict()
    for pair, insertion in read_input(14, input + '_2', [(str,)]):
        mapping_table[pair] = insertion
    return mapping_table


def get_score(state, first_char, last_char):
    number_of_chars = defaultdict(int)
    number_of_chars[first_char] += 1
    number_of_chars[last_char] += 1
    for [l, r], amount in state.items():
        number_of_chars[l] += amount
        number_of_chars[r] += amount
    return (max(number_of_chars.values()) - min(number_of_chars.values())) // 2


def part1(input, iterations):
    state, first_char, last_char = create_state(input)
    # print(state)

    mapping_table = create_mapping_table(input)
    # print(mapping_table)

    for iteration in range(iterations):
        new_state = defaultdict(int)
        for pair, instances in state.items():
            new_pair_left = pair[0] + mapping_table[pair]
            new_pair_right = mapping_table[pair] + pair[1]
            new_state[new_pair_left] += instances
            new_state[new_pair_right] += instances
        state = new_state
        # print(state)

    return get_score(state, first_char, last_char)


def part2(input):
    pass


if __name__ == '__main__':
    _, part, input, iterations = sys.argv
    if part == '1':
        print(part1(input, int(iterations)))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
