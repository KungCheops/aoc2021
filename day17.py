from helper.input import read_input_simple
import sys
import math


def hits_target(dx, dy, target_dimensions):
    xmin, xmax, ymin, ymax = target_dimensions

    x, y = 0, 0
    max_altitude_reached = 0

    while y >= ymin and x <= xmax:
        if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
            # print('hit target at: ', x, y)
            return max_altitude_reached
        x += dx
        y += dy
        if y > max_altitude_reached:
            max_altitude_reached = y
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1

    return -1


def part1(input):
    [xmin, xmax, ymin, ymax] = map(int, list(read_input_simple(17, input))[0].split())

    max_height = 0

    for y in range(0, 1000):
        for x in range(0, 1000):
            # print(x, y)
            height = hits_target(x, y, (xmin, xmax, ymin, ymax))
            if height > max_height:
                max_height = height

    return max_height


def part2(input):
    [xmin, xmax, ymin, ymax] = map(int, list(read_input_simple(17, input))[0].split())

    number_of_hits = 0

    min_dx = int((math.sqrt(8 * (xmin - 1) + 1) + 1) // 2)

    for y in range(ymin, -ymin):
        for x in range(min_dx, xmax + 1):
            # print(x, y)
            height = hits_target(x, y, (xmin, xmax, ymin, ymax))
            if height >= 0:
                number_of_hits += 1

    return number_of_hits


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
