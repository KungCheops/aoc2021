from helper.input import read_input
from collections import defaultdict
import sys


def parse_line(line):
    return [int(char) for char in line.strip()]


def part1(input):
    bit_buckets = defaultdict(int)
    lines = 0

    for [number] in read_input(3, input, [(parse_line,)]):
        for index, bit in enumerate(number):
            bit_buckets[index] += bit
        lines += 1

    most_common_bits = []
    for _index, value in sorted(bit_buckets.items()):
        most_common_bits.append(int(round(value / lines)))

    most_common_bits_string = ''.join(map(str, most_common_bits))
    least_common_bits_string = most_common_bits_string.replace('0', '2').replace('1', '0').replace('2', '1')
    most_common_number = int(most_common_bits_string, 2)
    least_common_number = int(least_common_bits_string, 2)

    return most_common_number * least_common_number


def filter_by_bit(numbers, bit_position, method):
    ratio = sum([number[bit_position] for number in numbers]) / len(numbers)
    if method == 'oxy':
        if ratio == 0.5:
            filter_by_bit = 1
        else:
            filter_by_bit = int(round(ratio))
    elif method == 'co2':
        if ratio == 0.5:
            filter_by_bit = 0
        else:
            filter_by_bit = 1 - int(round(ratio))
    return [number for number in numbers if number[bit_position] == filter_by_bit]


def get_rating(numbers, method):
    bit_position = 0
    while len(numbers) > 1:
        numbers = filter_by_bit(numbers, bit_position, method)
        bit_position += 1
    rating = int(''.join(map(str, numbers[0])), 2)
    return rating


def part2(input):
    all_numbers = []

    for [number] in read_input(3, input, [(parse_line,)]):
        all_numbers.append(number)

    return get_rating(all_numbers, 'oxy') * get_rating(all_numbers, 'co2')


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
