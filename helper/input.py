import re


def read_input(day, part):
    read_input(day, part, [str])


def read_input(day, part, fun_and_args):
    with open(f'input/day{day:02d}_{part}.txt') as file:
        for line in file:
            split_line = re.findall(r"[\w']+", line)
            extended_fun_and_args = fun_and_args
            while len(split_line) > len(extended_fun_and_args):
                extended_fun_and_args += fun_and_args

            typed_split_line = [fun(item, *args) for item, (fun, *args) in zip(split_line, fun_and_args)]
            yield typed_split_line
