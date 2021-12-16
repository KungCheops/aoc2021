from helper.input import read_input_simple
import sys
from functools import reduce


def convert_hex_to_binary(hex_string):
    return ''.join([f'{int(char, 16):04b}' for char in hex_string])


def parse_packet(binary_string):
    version = int(binary_string[0:3], 2)
    id = int(binary_string[3:6], 2)
    binary_string = binary_string[6:]
    # print('version:', version, 'id:', id)

    if id == 4:
        status_bit = '1'
        value_bits = []
        while status_bit == '1':
            status_bit = binary_string[0]
            value_bits.append(binary_string[1:5])
            binary_string = binary_string[5:]
        value = int(''.join(value_bits), 2)
        # print('value:', value)
        return version, binary_string
    else:
        status_bit = binary_string[0]
        # print('status_bit:', status_bit)
        binary_string = binary_string[1:]
        if status_bit == '0':
            length = int(binary_string[0:15], 2)
            binary_string = binary_string[15:]
            # print('length:', length)
            sub_packet_binary_string = binary_string[0:length]
            sub_version_sum = 0
            while len(sub_packet_binary_string) > 0:
                sub_packet_version, sub_packet_binary_string = parse_packet(sub_packet_binary_string)
                sub_version_sum += sub_packet_version
            return version + sub_version_sum, binary_string[length:]
        elif status_bit == '1':
            number_of_sub_packets = int(binary_string[0:11], 2)
            binary_string = binary_string[11:]
            sub_version_sum = 0
            for i in range(number_of_sub_packets):
                sub_packet_version, binary_string = parse_packet(binary_string)
                sub_version_sum += sub_packet_version
            return version + sub_version_sum, binary_string


def product(values):
    return reduce(lambda x, y: x * y, values)


def less_than(values):
    return 1 if values[0] < values[1] else 0


def greater_than(values):
    return 1 if values[0] > values[1] else 0


def equals_to(values):
    return 1 if values[0] == values[1] else 0


def parse_packet2(binary_string):
    version = int(binary_string[0:3], 2)
    id = int(binary_string[3:6], 2)
    binary_string = binary_string[6:]
    # print('version:', version, 'id:', id)
    # input()

    if id == 4:
        status_bit = '1'
        value_bits = []
        while status_bit == '1':
            status_bit = binary_string[0]
            value_bits.append(binary_string[1:5])
            binary_string = binary_string[5:]
        value = int(''.join(value_bits), 2)
        # print('value:', value)
        return value, binary_string
    else:
        if id == 0:
            operation = sum
        elif id == 1:
            operation = product
        elif id == 2:
            operation = min
        elif id == 3:
            operation = max
        elif id == 5:
            operation = greater_than
        elif id == 6:
            operation = less_than
        elif id == 7:
            operation = equals_to
        # print('operation:', operation)
        status_bit = binary_string[0]
        binary_string = binary_string[1:]
        if status_bit == '0':
            length = int(binary_string[0:15], 2)
            binary_string = binary_string[15:]
            sub_packet_binary_string = binary_string[0:length]
            values = []
            while len(sub_packet_binary_string) > 0:
                value, sub_packet_binary_string = parse_packet2(sub_packet_binary_string)
                values.append(value)
            value =  operation(values)
            # print(f'performing operation {operation} on values: {values} yields {value}')
            return value, binary_string[length:]
        elif status_bit == '1':
            number_of_sub_packets = int(binary_string[0:11], 2)
            binary_string = binary_string[11:]
            values = []
            for i in range(number_of_sub_packets):
                value, binary_string = parse_packet2(binary_string)
                values.append(value)
            value =  operation(values)
            # print(f'performing operation {operation} on values: {values} yields {value}')
            return value, binary_string


def part1(input_file):
    for hex_string in read_input_simple(16, input_file):
        binary_string = convert_hex_to_binary(hex_string)
        print(parse_packet(binary_string))

    return


def part2(input_file):
    for hex_string in read_input_simple(16, input_file):
        binary_string = convert_hex_to_binary(hex_string)
        print(parse_packet2(binary_string))

    return


if __name__ == '__main__':
    _, part, input_file = sys.argv
    if part == '1':
        print(part1(input_file))
    elif part == '2':
        print(part2(input_file))
    else:
        print('Part must be one of 1 or 2')
