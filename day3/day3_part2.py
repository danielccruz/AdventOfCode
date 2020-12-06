import numpy

trees = []

with open('input_file.txt') as input_file:
    for line in input_file.readlines():
        trees.append(line.strip())

POSITION_X = 0
POSITION_Y = 0
tree_counter = 0

movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
outputs = []
for elem in movements:
    while True:
        if POSITION_Y >= len(trees) or POSITION_X > len(trees[0]):
            outputs.append(tree_counter)
            break
        if trees[POSITION_Y][POSITION_X] == '#':
            tree_counter = tree_counter + 1
        POSITION_X = POSITION_X + elem[0]
        POSITION_X = POSITION_X % len(trees[0])
        POSITION_Y = POSITION_Y + elem[1]
    POSITION_X = 0
    POSITION_Y = 0
    tree_counter = 0

print(numpy.prod(outputs))
