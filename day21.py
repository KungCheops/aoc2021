from helper.input import read_input
import sys
from collections import defaultdict


def part1(input):
    player_positions = dict()
    player_scores = defaultdict(int)

    [[a_start_pos, b_start_pos]] = read_input(21, input, [(int,)])
    player_positions[0] = a_start_pos - 1
    player_positions[1] = b_start_pos - 1

    dice_value = 1
    die_rolls = 0
    while True:
        for id in player_positions:
            die_sum = 0
            for i in range(3):
                die_sum += dice_value
                dice_value += 1
                if dice_value == 101:
                    dice_value = 1
            die_rolls += 3
            player_positions[id] += die_sum
            player_positions[id] %= 10
            player_scores[id] += player_positions[id] + 1
            if player_scores[id] >= 1000:
                # print(f'Player {id} has {player_scores[id]} points')
                return player_scores[(id + 1) % 2] * die_rolls


def part2(input):
    [[a_start_pos, b_start_pos]] = read_input(21, input, [(int,)])
    state = defaultdict(int)
    state[(a_start_pos - 1, 0, b_start_pos - 1, 0)] = 1
    possible_steps = ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1))

    a_wins = 0
    b_wins = 0
    iterations = 0

    while len(state) > 0:
        new_state = defaultdict(int)
        for (a_pos, a_score, b_pos, b_score), universes in state.items():
            # A plays
            for a_steps, a_times in possible_steps:
                a_pos_new = (a_pos + a_steps) % 10
                a_score_new = a_score + a_pos_new + 1
                if a_score_new >= 21:
                    a_wins += universes * a_times
                else:
                    # new_state[(a_pos_new, a_score_new, b_pos, b_score)] += universes * a_times
                    # B plays
                    for b_steps, b_times in possible_steps:
                        b_pos_new = (b_pos + b_steps) % 10
                        b_score_new = b_score + b_pos_new + 1
                        if b_score_new >= 21:
                            b_wins += universes * a_times * b_times
                        else:
                            new_state[(a_pos_new, a_score_new, b_pos_new, b_score_new)] += universes * a_times * b_times
        state = new_state
        iterations += 1
        print(f'Iterations: {iterations}, number of unique states: {len(state)}')

    if a_wins > b_wins:
        print(f'Player 1 won with {a_wins} wins over player 2 with {b_wins} wins. ({a_wins / b_wins} times the score)')
    else:
        print(f'Player 2 won with {b_wins} wins over player 1 with {a_wins} wins. ({b_wins / a_wins} times the score)')
    return max(a_wins, b_wins)


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
