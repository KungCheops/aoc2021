from helper.input import read_input
import sys
from collections import defaultdict


def part1(input):
    counter = 0
    for line in read_input(8, input, [(str,)]):
        input, output = line
        # print(f'input: {input}')
        # print(f'output: {output}')
        for item in output:
            if len(item) in [2, 3, 4, 7]:
                counter += 1
    return counter


def convert_to_number(input, segment_mapping):
    lit_up = set()
    for char in input:
        lit_up.add(segment_mapping[char])
    if lit_up == {0, 1, 2, 4, 5, 6}:
        return 0
    elif lit_up == {2, 5}:
        return 1
    elif lit_up == {0, 2, 3, 4, 6}:
        return 2
    elif lit_up == {0, 2, 3, 5, 6}:
        return 3
    elif lit_up == {1, 2, 3, 5}:
        return 4
    elif lit_up == {0, 1, 3, 5, 6}:
        return 5
    elif lit_up == {0, 1, 3, 4, 5, 6}:
        return 6
    elif lit_up == {0, 2, 5}:
        return 7
    elif lit_up == {0, 1, 2, 3, 4, 5, 6}:
        return 8
    elif lit_up == {0, 1, 2, 3, 5, 6}:
        return 9
    else:
        return -1


def part2(input):
    sum = 0
    for line in read_input(8, input, [(str,)]):
        input, output = line
        segment = dict()
        segment_inverse = dict()
        items_by_length = defaultdict(list)
        for item in input:
            items_by_length[len(item)].append(set(item))

        # deduce segment 0
        segment[0] = (items_by_length[3][0] - items_by_length[2][0]).pop()

        # deduce segment 5
        for len6 in items_by_length[6]:
            intersect = len6.intersection(items_by_length[2][0])
            if len(intersect) == 1:
                segment[5] = intersect.pop()
                break

        # deduce segment 2
        segment[2] = (items_by_length[2][0] - {segment[5]}).pop()

        # deduce segment 3
        len4_minus_2_and_5 = items_by_length[4][0] - {segment[2], segment[5]}
        for len5 in items_by_length[5]:
            intersect = len5.intersection(len4_minus_2_and_5)
            if len(intersect) == 1:
                segment[3] = intersect.pop()
                break

        # deduce segment 1
        segment[1] = (len4_minus_2_and_5 - {segment[3]}).pop()

        # deduce segment 6
        for len6 in items_by_length[6]:
            difference = len6 - {segment[0], segment[1], segment[2], segment[3], segment[5]}
            if len(difference) == 1:
                segment[6] = difference.pop()
                break

        # deduce segment 4
        segment[4] = ({'a', 'b', 'c', 'd', 'e', 'f', 'g'} - set(segment.values())).pop()

        for i in range(7):
            segment_inverse[segment[i]] = i

        sum += int(''.join([str(convert_to_number(item, segment_inverse)) for item in output]))

    return sum


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
