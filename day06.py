from helper.input import read_input
import sys


def part1(input):
    file, days = input
    days = int(days)
    [state] = read_input(6, file, [(int,)])
    # print(f'Initial state: {state}')

    for day in range(days):
        for index, value in enumerate(state):
            state[index] = value - 1
            if state[index] == -1:
                state[index] = 6
                state.append(9)
        # print(f'After {day + 1: 3d} days: {state} (total fish: {len(state)})')

    return len(state)


def part2(input):
    file, days = input
    days = int(days)
    [initial_state] = read_input(6, file, [(int,)])
    days_remaining = [0] * 9
    for fish_state in initial_state:
        days_remaining[fish_state] += 1
    # print(f'Initial state: {days_remaining}')

    for day in range(days):
        giving_birth = days_remaining[0]
        for index in range(0, len(days_remaining) - 1):
            days_remaining[index] = days_remaining[index + 1]
        days_remaining[6] += giving_birth
        days_remaining[8] = giving_birth
        # print(f'After {day + 1: 3d} days: {days_remaining} (total fish: {sum(days_remaining)})')

    return sum(days_remaining)


if __name__ == '__main__':
    _, part, *input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
