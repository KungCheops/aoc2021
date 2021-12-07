from helper.input import read_input
import sys
import numpy as np


def part1(input):
    [crab_positions] = read_input(7, input, [(int,)])

    crab_positions = np.array(crab_positions, dtype=int)

    min_x = np.min(crab_positions)
    max_x = np.max(crab_positions)

    cost_of_going_to_x = np.array([0] * (max_x - min_x + 1), dtype=int)

    for crab_position in crab_positions:
        for i in range(min_x, max_x + 1):
            cost_of_going_to_x[i] += np.abs(crab_position - i)

    return np.min(cost_of_going_to_x)


def cost(a, b):
    distance = np.abs(a - b)
    return (distance * (distance + 1)) // 2


def part2(input):
    [crab_positions] = read_input(7, input, [(int,)])

    crab_positions = np.array(crab_positions, dtype=int)

    min_x = np.min(crab_positions)
    max_x = np.max(crab_positions)

    cost_of_going_to_x = np.array([0] * (max_x - min_x + 1), dtype=int)

    for crab_position in crab_positions:
        for i in range(min_x, max_x + 1):
            cost_of_going_to_x[i] += cost(crab_position, i)

    return np.min(cost_of_going_to_x)


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
