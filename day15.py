from helper.input import read_input_simple
import sys
import numpy as np
from heapq import *


def create_map(input):
    map = list()
    for line in read_input_simple(15, input):
        map.append([int(char) for char in line])
    return np.array(map, dtype=int)


def get_map_value(map, x, y):
    if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
        return 99999999999

    return map[y][x]


def get_map_value2(map, x, y):
    if x < 0 or y < 0 or x >= len(map[0]) * 5 or y >= len(map) * 5:
        return 99999999999

    x_in_map = x % len(map[0])
    y_in_map = y % len(map)

    x_map = x // len(map[0])
    y_map = y // len(map)

    additional_cost = x_map + y_map

    map_value = map[y_in_map][x_in_map] + additional_cost

    map_value = ((map_value - 1) % 9) + 1

    return map_value


def find_path(map, start_position, end_position, map_value_function):
    processed = set()
    previous_node = dict()
    to_visit = list()
    heappush(to_visit, (0, start_position))
    processed.add(start_position)
    distance_to_node = dict()

    while len(to_visit) > 0:
        cost, current_node = heappop(to_visit)
        # print(f'exploring node: {current_node}')
        # print(f'distance to node: {cost}')
        # print(f'processed so far: {processed}')
        distance_to_node[current_node] = cost

        if current_node == end_position:
            break

        for x_offset, y_offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbor_x = current_node[0] + x_offset
            neighbor_y = current_node[1] + y_offset
            neighbor_position = (neighbor_x, neighbor_y)
            if not neighbor_position in processed:
                heappush(to_visit, (cost + map_value_function(map, neighbor_x, neighbor_y), neighbor_position))
                processed.add(neighbor_position)
                previous_node[neighbor_position] = current_node
        # print(f'To visit: {to_visit}')
    path = []
    previous_position = end_position
    while previous_position != start_position:
        path.append((previous_position, distance_to_node[previous_position]))
        previous_position = previous_node[previous_position]
    return reversed(path)



def part1(input):
    map = create_map(input)
    start_position = (0, 0)
    end_position = (map.T.shape[0] - 1, map.T.shape[1] - 1)

    # print(map)

    path = find_path(map, start_position, end_position, get_map_value)

    return list(path)[-1][1]


def part2(input):
    map = create_map(input)
    start_position = (0, 0)
    end_position = (map.T.shape[0] * 5 - 1, map.T.shape[1] * 5 - 1)

    # print(map)

    path = find_path(map, start_position, end_position, get_map_value2)

    return list(path)[-1][1]


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
