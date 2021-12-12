from helper.input import read_input
import sys
from collections import defaultdict


def create_graph(input):
    paths = defaultdict(list)
    for source, target in read_input(12, input, [(str,)]):
        if target != 'start' and source != 'end':
            paths[source].append(target)
        if target != 'end' and source != 'start':
            paths[target].append(source)
    return paths


def sub_paths(node, graph, previous_small_nodes=set()):
    if node == 'end':
        return (node, [])
    if node.islower():
        next_small_nodes = previous_small_nodes | {node}
    else:
        next_small_nodes = previous_small_nodes
    return (node, [sub_paths(next_node, graph, next_small_nodes) for next_node in graph[node] if not next_node in next_small_nodes])


def sub_paths2(node, graph, previous_small_nodes=defaultdict(int), used_double=False):
    if node == 'end':
        return (node, [])
    if node.islower():
        next_small_nodes = previous_small_nodes.copy()
        next_small_nodes[node] += 1
    else:
        next_small_nodes = previous_small_nodes
    return (node, [sub_paths2(next_node, graph, next_small_nodes, used_double or next_small_nodes[next_node] == 1) for next_node in graph[node] if next_small_nodes[next_node] < 1 or next_small_nodes[next_node] < 2 and not used_double])


def number_of_sub_paths(sub_paths):
    if sub_paths == []:
        return 0
    elif sub_paths == ('end', []):
        return 1
    else:
        return sum([number_of_sub_paths(sub_sub_path) for sub_sub_path in sub_paths[1]])


def print_paths(sub_paths, previous_steps=[]):
    if sub_paths == []:
        return
    elif sub_paths == ('end', []):
        print(previous_steps + ['end'])
        return
    else:
        return [print_paths(sub_sub_path, previous_steps + [sub_paths[0]]) for sub_sub_path in sub_paths[1]]


def number_of_paths(input, sub_paths_method):
    graph = create_graph(input)
    print(graph)
    paths = sub_paths_method('start', graph)
    # print_paths(paths)
    return number_of_sub_paths(paths)


def part1(input):
    return number_of_paths(input, sub_paths)


def part2(input):
    return number_of_paths(input, sub_paths2)


if __name__ == '__main__':
    _, part, input = sys.argv
    if part == '1':
        print(part1(input))
    elif part == '2':
        print(part2(input))
    else:
        print('Part must be one of 1 or 2')
