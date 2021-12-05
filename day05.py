from helper.input import read_input
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import sys
import re


def inclusive_range(start, end):
    if start <= end:
        return range(start, end + 1)
    else:
        return range(start, end - 1, -1)


def print_board(board, minX, maxX, minY, maxY):
    np_arr = np.zeros([maxY - minY + 1, maxX - minX + 1], dtype=int)
    for y in inclusive_range(minY, maxY):
        for x in inclusive_range(minX, maxX):
            np_arr[y][x] = board[(x, y)]
    plt.pause(1)
    plt.imshow(np_arr, interpolation='nearest')


def part1(input):
    return number_of_intersections(1, input)


def part2(input):
    return number_of_intersections(2, input)


def number_of_intersections(part, input):
    game_board = defaultdict(int)
    minY = maxY = minX = maxX = 0

    intersections = 0
    maxIntersecting = 0

    for [startX, startY, endX, endY] in read_input(5, input, [(int,)]):
        local_minX = min(startX, endX)
        local_maxX = max(startX, endX)
        local_minY = min(startY, endY)
        local_maxY = max(startY, endY)

        if local_minX < minX:
            minX = local_minX
        if local_minY < minY:
            minY = local_minY
        if local_maxX > maxX:
            maxX = local_maxX
        if local_maxY > maxY:
            maxY = local_maxY

        if startX == endX:
            for y in inclusive_range(startY, endY):
                game_board[(startX, y)] += 1
                print_board(game_board, minX, maxX, minY, maxY)
                if game_board[(startX, y)] == 2:
                    intersections += 1
                if game_board[(startX, y)] > maxIntersecting:
                    maxIntersecting = game_board[(startX, y)]
        elif startY == endY:
            for x in inclusive_range(startX, endX):
                game_board[(x, startY)] += 1
                print_board(game_board, minX, maxX, minY, maxY)
                if game_board[(x, startY)] == 2:
                    intersections += 1
                if game_board[(x, startY)] > maxIntersecting:
                    maxIntersecting = game_board[(x, startY)]
        elif part == 2:
            for x, y in zip(inclusive_range(startX, endX), inclusive_range(startY, endY)):
                game_board[(x, y)] += 1
                print_board(game_board, minX, maxX, minY, maxY)
                if game_board[(x, y)] == 2:
                    intersections += 1
                if game_board[(x, y)] > maxIntersecting:
                    maxIntersecting = game_board[(x, y)]
    plt.colorbar()
    plt.show()
    return intersections


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
