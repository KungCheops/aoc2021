from helper.input import read_input
import sys
import numpy as np
import time
from functools import reduce
from matplotlib import pyplot as plt


def create_map(input):
    map = list()
    for [line] in read_input(9, input, [(str,)]):
        map.append([int(char) for char in line])
    return np.array(map, dtype=int)


def get_height(x, y, map):
    if y >= 0 and y < len(map) and x >= 0 and x < len(map[y]):
        return map[y][x]
    return 9


def lower_than_neighbors(height, x, y, map, ignore_coords=set(), strict=False):
    if height == 9:
        return False
    if strict:
        c1 = ((x, y - 1) in ignore_coords or height < get_height(x, y - 1, map))
        c2 = ((x, y + 1) in ignore_coords or height < get_height(x, y + 1, map))
        c3 = ((x - 1, y) in ignore_coords or height < get_height(x - 1, y, map))
        c4 = ((x + 1, y) in ignore_coords or height < get_height(x + 1, y, map))
    else:
        c1 = ((x, y - 1) in ignore_coords or height <= get_height(x, y - 1, map))
        c2 = ((x, y + 1) in ignore_coords or height <= get_height(x, y + 1, map))
        c3 = ((x - 1, y) in ignore_coords or height <= get_height(x - 1, y, map))
        c4 = ((x + 1, y) in ignore_coords or height <= get_height(x + 1, y, map))
    return c1 and c2 and c3 and c4


def part1(input):
    map = create_map(input)
    lowest_points = np.zeros(map.shape)
    risk_level = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            height = map[y][x]
            if lower_than_neighbors(height, x, y, map):
                risk_level += height + 1
    return risk_level


def create_basin(x, y, map):
    to_explore_tiles = [(map[y][x], x, y)]
    basin_tiles_map = np.zeros(map.shape, dtype=int)
    explored_tiles = set()
    basin_tiles = set()
    ignore_coords = set()
    iter = 0
    while len(to_explore_tiles) > 0:
        # print('to explore: ', to_explore_tiles)
        current_tile = to_explore_tiles[0]
        # print('current tile: ', current_tile)
        to_explore_tiles = to_explore_tiles[1:]
        height, x, y = current_tile
        explored_tiles.add(current_tile)
        # print(current_tile, explored_tiles, to_explore_tiles)
        if lower_than_neighbors(height, x, y, map, ignore_coords):
            # print('lower than neighbors')
            basin_tiles.add(current_tile)
            ignore_coords.add((x, y))
            basin_tiles_map[y][x] = 1
            for neighbor_x, neighbor_y in ((x, y - 1),(x, y + 1),(x - 1, y),(x + 1, y)):
                # print('neighbor coordinates: ', neighbor_x, neighbor_y)
                if neighbor_y >= 0 and neighbor_y < len(map) and neighbor_x >= 0 and neighbor_x < len(map[neighbor_y]):
                    neighbor_height = map[neighbor_y][neighbor_x]
                    if not (neighbor_height, neighbor_x, neighbor_y) in to_explore_tiles and not (neighbor_height, neighbor_x, neighbor_y) in explored_tiles:
                        # print(neighbor_x, neighbor_y, neighbor_height)
                        to_explore_tiles.append((neighbor_height, neighbor_x, neighbor_y))
            to_explore_tiles = sorted(to_explore_tiles)
        iter += 1
    return len(basin_tiles), basin_tiles_map


def part2(input):
    map = create_map(input)
    lowest_points = np.zeros(map.shape, dtype=int)
    basins = list()
    for y in range(len(map)):
        for x in range(len(map[y])):
            height = map[y][x]
            if lower_than_neighbors(height, x, y, map, strict=True):
                basin_size, basin_map = create_basin(x, y, map)
                basins.append(basin_size)
                lowest_points += basin_map
                # print(x, y, height)
                lowest_points[y][x] += 1
    # print(lowest_points)
    plt.subplot(2, 1, 1)
    plt.imshow(map, interpolation='nearest')
    plt.subplot(2, 1, 2)
    plt.imshow(lowest_points, interpolation='nearest')
    plt.show()
    print(lowest_points)
    return reduce(lambda x, y: x * y, sorted(basins)[-3:])


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
