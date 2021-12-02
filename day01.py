from lib.input import read_input
import sys

def part1(input):
    increased = 0
    last_value = 1000000 # max value in input: 10000

    for [value] in read_input(1, input, [int]):
        if value > last_value:
            increased += 1
        last_value = value

    return increased

def part2(input):
    increased = 0
    moving_sum = [10000, 10000, 10000]
    last_sum = 30000
    index = 0

    for [partial_value] in read_input(1, input, [int]):
        moving_sum[index % 3] = partial_value
        index += 1
        current_sum = sum(moving_sum)
        if current_sum > last_sum:
            increased += 1
        last_sum = current_sum

    return increased

if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
