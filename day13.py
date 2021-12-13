from helper.input import read_input
import sys


def create_map(input):
    input1 = input + '_1'
    map = set()
    max_x = 0
    max_y = 0
    for x, y in read_input(13, input1, [(int,)]):
        map.add((x, y))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    return map, (max_x + 1, max_y + 1)


def get_folds(input):
    input2 = input + '_2'
    folds = list()
    for _, _, axis, location in read_input(13, input2, [(str,), (str,), (str,), (int,)]):
        folds.append((axis, location))
    return folds


def fold_map(map, fold, dimensions):
    axis, location = fold
    max_x, max_y = dimensions
    new_max_x, new_max_y = 0, 0
    new_map = set()
    if axis == 'y':
        for x, y in map:
            new_x, new_y = x, y
            if y >= location:
                if y == location:
                    print(f'error: y={y} is on the folding line')
                new_y = y - 2 * (y - location)
            new_map.add((new_x, new_y))
            if new_x > new_max_x:
                new_max_x = new_x
            if new_y > new_max_y:
                new_max_y = new_y
    if axis == 'x':
        for x, y in map:
            new_x, new_y = x, y
            if x >= location:
                if x == location:
                    print(f'error: x={x} is on the folding line')
                new_x = x - 2 * (x - location)
            new_map.add((new_x, new_y))
            if new_x > new_max_x:
                new_max_x = new_x
            if new_y > new_max_y:
                new_max_y = new_y
    return new_map, (new_max_x + 1, new_max_y + 1)


def map_to_string(map, dimensions):
    return '\n'.join([''.join(['#' if (x, y) in map else '.' for x in range(dimensions[0])]) for y in range(dimensions[1])])


def part1(input):
    map, dimensions = create_map(input)
    folds = get_folds(input)
    map, dimensions = fold_map(map, folds[0], dimensions)
    return len(map)


def part2(input):
    map, dimensions = create_map(input)
    folds = get_folds(input)
    for fold in folds:
        map, dimensions = fold_map(map, fold, dimensions)
    return map_to_string(map, dimensions)


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
