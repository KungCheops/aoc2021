from helper.input import read_input_simple
import sys
import numpy as np
import matplotlib.pyplot as plt
import time


def create_map(input):
    [input_line] = list(read_input_simple(20, input + '_1'))
    map = dict()
    for i, char in enumerate(input_line):
        if char == '#':
            map[i] = 1
        elif char == '.':
            map[i] = 0
    return map


def create_image(input):
    image = set()
    max_x, max_y = 0, 0
    for y, line in enumerate(read_input_simple(20, input + '_2')):
        for x, char in enumerate(line):
            if char == '#':
                image.add((x, y))
    return image, (0, x, 0, y)


def get_value(x, y, image):
    bit_string = ''
    for y2 in range(y - 1, y + 2):
        for x2 in range(x - 1, x + 2):
            if (x2, y2) in image:
                bit_string += '1'
            else:
                bit_string += '0'
    return int(bit_string, 2)


def image_to_string(image, minX, maxX, minY, maxY):
    string = ''
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            string += '#' if (x, y) in image else '.'
        string += '\n'
    return string


def image_to_nparray(image, minX, maxX, minY, maxY, padding=0):
    draw_array = np.zeros((maxY - minY + 1 + padding * 2, maxX - minX + 1 + padding * 2), dtype=int)

    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if (x, y) in image:
                draw_array[y - minY + padding][x - minX + padding] = 1

    return draw_array


def image_enhance(input, iterations):
    map = create_map(input)
    image, (minX, maxX, minY, maxY) = create_image(input)
    plt.ion()
    figure, ax = plt.subplots(figsize=(10, 8))
    data = image_to_nparray(image, minX, maxX, minY, maxY, padding=3)
    line = plt.imshow(data, interpolation='nearest')

    for i in range(iterations):
        new_image = set()
        new_minX, new_maxX, new_minY, new_maxY = 0, 0, 0, 0
        if i % 2 == 0:
            y_range = range(minY - 3, maxY + 4)
            x_range = range(minX - 3, maxX + 4)
        else:
            y_range = range(minY - 1, maxY + 2)
            x_range = range(minX - 1, maxX + 2)
        for y in y_range:
            for x in x_range:
                if map[get_value(x, y, image)] == 1:
                    new_image.add((x, y))
                    if i % 2 == 1 or x >= minX - 1 and x <= maxX + 1:
                        if x < new_minX:
                            new_minX = x
                        if x > new_maxX:
                            new_maxX = x
                    if i % 2 == 1 or y >= minY - 1 and y <= maxY + 1:
                        if y < new_minY:
                            new_minY = y
                        if y > new_maxY:
                            new_maxY = y

        image = new_image
        minX, maxX, minY, maxY = new_minX, new_maxX, new_minY, new_maxY
        line.set_data(image_to_nparray(image, minX, maxX, minY, maxY, padding=3))
        figure.canvas.draw()
        figure.canvas.flush_events()
        time.sleep(0.1)
    plt.show()
    return len(image)


def part1(input):
    return image_enhance(input, 2)


def part2(input, iterations):
    return image_enhance(input, iterations)


if __name__ == '__main__':
    _, part, input, *iterations = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input, int(iterations[0])))
    else:
        print('Part must be one of 1 or 2')
