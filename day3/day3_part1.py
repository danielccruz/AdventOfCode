trees = []

with open('input_file.txt') as input_file:
    for line in input_file.readlines():
        trees.append(line.strip())

POSITION_X = 0
POSITION_Y = 0
tree_counter = 0

while True:
    if POSITION_Y >= len(trees) or POSITION_X > len(trees[0]):
        print(tree_counter)
        break
    if trees[POSITION_Y][POSITION_X] == '#':
        tree_counter = tree_counter + 1
    POSITION_X = POSITION_X + 3
    POSITION_X = POSITION_X % len(trees[0])
    POSITION_Y = POSITION_Y + 1




