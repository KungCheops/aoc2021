from lib.input import read_input
import sys

def part1(input):
    forward = 0
    depth = 0
    for command, distance in read_input(2, input, [str, int]):
        if command == 'forward':
            forward += distance
        elif command == 'down':
            depth += distance
        elif command =='up':
            depth -= distance
    print(f'hpos: {forward}, depth: {depth}')
    return forward * depth

def part2(input):
    forward = 0
    depth = 0
    aim = 0
    for command, amount in read_input(2, input, [str, int]):
        if command == 'forward':
            forward += amount
            depth += amount * aim
        elif command == 'down':
            aim += amount
        elif command =='up':
            aim -= amount
    print(f'hpos: {forward}, depth: {depth}')
    return forward * depth

if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
