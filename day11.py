from helper.input import read_input
import sys
import numpy as np


def create_map(input):
    map = list()
    for [line] in read_input(11, input, [(str,)]):
        map.append([int(char) for char in line])
    return np.array(map, dtype=int)


def part1(input, iterations):
    map = create_map(input)
    count = 0
    for i in range(iterations):
        map += 1
        flash_spots = np.where(map == 10)
        already_flashed = set()
        anything_happened = True
        while anything_happened:
            anything_happened = False
            for y, x in zip(flash_spots[0], flash_spots[1]):
                if not (x, y) in already_flashed:
                    anything_happened = True
                    count += 1
                    for x_offset in (-1, 0, 1):
                        for y_offset in (-1, 0, 1):
                            neighbor_x = x + x_offset
                            neighbor_y = y + y_offset
                            if neighbor_y >= 0 and neighbor_y < len(map) and neighbor_x >= 0 and neighbor_x < len(map[neighbor_y]):
                                map[neighbor_y][neighbor_x] += 1
                already_flashed.add((x, y))
            flash_spots = np.where(map > 9)
        map[np.where(map > 9)] = 0
    return count


def part2(input):
    map = create_map(input)
    i = 0
    time_per_iteration = []
    while True:
        map += 1
        flash_spots = np.where(map == 10)
        already_flashed = set()
        anything_happened = True
        while anything_happened:
            anything_happened = False
            for y, x in zip(flash_spots[0], flash_spots[1]):
                if not (x, y) in already_flashed:
                    anything_happened = True
                    for x_offset in (-1, 0, 1):
                        for y_offset in (-1, 0, 1):
                            neighbor_x = x + x_offset
                            neighbor_y = y + y_offset
                            if neighbor_y >= 0 and neighbor_y < len(map) and neighbor_x >= 0 and neighbor_x < len(map[neighbor_y]):
                                map[neighbor_y][neighbor_x] += 1
                already_flashed.add((x, y))
            flash_spots = np.where(map > 9)
        map[np.where(map > 9)] = 0
        i += 1
        if np.all(map == 0):
            return i


if __name__ == '__main__':
    _, part, input, *iterations = sys.argv
    if part == '1':
        print(part1(input, int(iterations[0])))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
