from helper.input import read_input_simple
import sys


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


def depth(tree):
    if type(tree) == int:
        return -1
    else:
        return 1 + max(depth(tree[0]), depth(tree[1]))


class number:
    def __init__(self, linear_representation, nested_representation):
        self.linear_representation = linear_representation
        self.nested_representation = nested_representation


    @classmethod
    def fromstring(cls, string):
        linear_representation = [int(num) for num in string if num.isnumeric()]
        nested_representation = create_number(string)
        return cls(linear_representation, nested_representation)


    def __repr__(self):
        return self.linear_representation, self.nested_representation


    @classmethod
    def add(_, a, b):
        a_linear, a_nested = a.linear_representation, a.nested_representation
        b_linear, b_nested = b.linear_representation, b.nested_representation

        return_linear = a_linear + b_linear
        return_nested = (a_nested, b_nested)

        return number(return_linear, return_nested)


    def will_reduce(self):
        max_depth = depth(self.nested_representation)
        any_value_over_nine = any(value > 9 for value in self.linear_representation)
        return max_depth > 4 or any_value_over_nine


    def reduce(self):
        if depth(self.nested_representation) > 4:
            self.explode()
        elif any(value > 9 for value in self.linear_representation):
            self.split()


    def explode(self):
        return



def part1(input):
    sum = None
    for line in read_input_simple(18, input):
        if sum is None:
            sum = number.fromstring(line)
        else:
            sum = number.add(sum, number.fromstring(line))
            print(sum.will_reduce())
            # while sum.will_reduce():
            #     sum = sum.reduce()
        print(f'Sum (linear): {sum.linear_representation}')
        print(f'Sum (nested): {sum.nested_representation}')


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
