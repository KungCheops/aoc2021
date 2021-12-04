from helper.input import read_input
from collections import defaultdict
import sys
import numpy


def winning_board(board):
    numpy_board = numpy.array(board)
    for row in numpy_board:
        if numpy.all(row):
            return True
    for col in numpy_board.T:
        if numpy.all(col):
            return True
    return False


def part1(input):
    board_index = -1
    board_states = defaultdict(list)
    board_values_uncalled = defaultdict(set)
    position_of = defaultdict(lambda:False)
    for index, line in enumerate(read_input(4, input, [(int,)])):
        if index == 0:
            winning_numbers = line
        elif line == []:
            board_index += 1
            board_row_index = 0
        else:
            for board_col_index, value in enumerate(line):
                position_of[(board_index, value)] = (board_row_index, board_col_index)
                board_values_uncalled[board_index].add(value)
            board_row_index += 1
            board_states[board_index].append([False for _ in line])

    for winning_number in winning_numbers:
        for board_id, board_state in board_states.items():
            if pos := position_of[(board_id, winning_number)]:
                row, col = pos
                board_state[row][col] = True
                board_values_uncalled[board_id].remove(winning_number)
                if winning_board(board_state):
                    return sum(board_values_uncalled[board_id]) * winning_number

    return boards


def part2(input):
    board_index = -1
    board_states = defaultdict(list)
    board_values_uncalled = defaultdict(set)
    position_of = defaultdict(lambda:False)
    boards_that_have_not_won = set()
    for index, line in enumerate(read_input(4, input, [(int,)])):
        if index == 0:
            winning_numbers = line
        elif line == []:
            board_index += 1
            boards_that_have_not_won.add(board_index)
            board_row_index = 0
        else:
            for board_col_index, value in enumerate(line):
                position_of[(board_index, value)] = (board_row_index, board_col_index)
                board_values_uncalled[board_index].add(value)
            board_row_index += 1
            board_states[board_index].append([False for _ in line])

    for winning_number in winning_numbers:
        for board_id, board_state in board_states.items():
            if board_id in boards_that_have_not_won:
                if pos := position_of[(board_id, winning_number)]:
                    row, col = pos
                    board_state[row][col] = True
                    board_values_uncalled[board_id].remove(winning_number)
                    if winning_board(board_state):
                        boards_that_have_not_won.remove(board_id)
                        if len(boards_that_have_not_won) == 0:
                            return sum(board_values_uncalled[board_id]) * winning_number

    return boards



if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
