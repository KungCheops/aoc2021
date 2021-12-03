def read_input(day, part):
    read_input(day, part, [str])

def read_input(day, part, type_and_args):
    with open(f'input/day{day:02d}_{part}.txt') as file:
        for line in file:
            split_line = line.split(' ')
            typed_split_line = [type(item, *args) for item, (type, *args) in zip(split_line, type_and_args)]
            yield typed_split_line
