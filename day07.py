from helper.input import read_input
import sys
from collections import defaultdict


def cost1(a, b):
    return abs(a - b)


def cost2(a, b):
    distance = abs(a - b)
    return (distance * (distance + 1)) // 2


def get_min_distance(input, distance_function):
    [crab_positions] = read_input(7, input, [(int,)])

    min_x = min(crab_positions)
    max_x = max(crab_positions)

    crabs_at_positions = defaultdict(int)

    for crab_position in crab_positions:
        crabs_at_positions[crab_position] += 1

    cost_of_going_to_x = [0] * (max_x - min_x + 1)

    for crab_position, crabs_at_position in crabs_at_positions.items():
        if crabs_at_position != 0:
            for i in range(min_x, max_x + 1):
                cost_of_going_to_x[i] += distance_function(crab_position, i) * crabs_at_position

    return min(cost_of_going_to_x)


def part1(input):
    return get_min_distance(input, cost1)


def part2(input):
    return get_min_distance(input, cost2)


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
