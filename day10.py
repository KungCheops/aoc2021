from helper.input import read_input_simple
import sys
from collections import defaultdict


def part1(input):
    score = 0
    for line in read_input_simple(10, input):
        stack = list()
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif char == ')':
                if not stack.pop() == '(':
                    score += 3
                    break
            elif char == ']':
                if not stack.pop() == '[':
                    score += 57
                    break
            elif char == '}':
                if not stack.pop() == '{':
                    score += 1197
                    break
            elif char == '>':
                if not stack.pop() == '<':
                    score += 25137
                    break
    return score


def part2(input):
    scores = list()
    for line in read_input_simple(10, input):
        stack = list()
        incomplete = False
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif char == ')':
                if not stack.pop() == '(':
                    incomplete = True
                    break
            elif char == ']':
                if not stack.pop() == '[':
                    incomplete = True
                    break
            elif char == '}':
                if not stack.pop() == '{':
                    incomplete = True
                    break
            elif char == '>':
                if not stack.pop() == '<':
                    incomplete = True
                    break
        if not incomplete:
            line_score = 0
            for item in reversed(stack):
                line_score *= 5
                if item == '(':
                    line_score += 1
                if item == '[':
                    line_score += 2
                if item == '{':
                    line_score += 3
                if item == '<':
                    line_score += 4
            scores.append(line_score)
    return sorted(scores)[(len(scores)) // 2]


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
