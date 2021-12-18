from helper.input import read_input_simple
import sys


class number:
    # TODO


def find_matching_comma_and_bracket(number_string):
    depth = 0
    comma_index = -1
    for i, char in enumerate(number_string):
        if depth == 1 and char == ',':
            comma_index = i
        elif depth == 1 and char == ']':
            return comma_index, i
        elif char == '[':
            depth += 1
        elif char == ']':
            depth -= 1


def create_number(number_string):
    if number_string[0] == '[':
        comma_index, end_bracket_index = find_matching_comma_and_bracket(number_string)
        return (create_number(number_string[1:comma_index]), create_number(number_string[comma_index + 1:end_bracket_index]))
    else:
        return int(number_string)



def parse_number(number_string):
    linear_representation = [int(num) for num in number_string if num.isnumeric()]
    nested_representation = create_number(number_string)
    return linear_representation, nested_representation


def add_numbers(a, b):
    a_linear, a_nested = a
    b_linear, b_nested = b

    return_linear = a_linear + b_linear
    return_nested = (a_nested, b_nested) if a_nested else b_nested

    return return_linear, return_nested





def part1(input):
    sum_nested = None
    sum_linear = []
    for line in read_input_simple(18, input):
        sum_linear, sum_nested = add_numbers((sum_linear, sum_nested), parse_number(line))
        print(f'Sum (linear): {sum_linear}')
        print(f'Sum (nested): {sum_nested}')


def part2(input):
    pass


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
