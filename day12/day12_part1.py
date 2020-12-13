instructions = [line.rstrip('\n') for line in open('../day12/input_file.txt')]

normalized_instructions = []
for instruction in instructions:
    normalized_instructions.append((instruction[0:1], int(instruction[1:])))

DIRECTION = 'E'
COORD_X = 0
COORD_Y = 0

d_r = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}
d_l = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}

for instruction in normalized_instructions:
    if instruction[0] == 'N':
        COORD_Y += instruction[1]
    elif instruction[0] == 'S':
        COORD_Y -= instruction[1]
    elif instruction[0] == 'E':
        COORD_X += instruction[1]
    elif instruction[0] == 'W':
        COORD_X -= instruction[1]
    elif instruction[0] == 'L':
        n_rotations = instruction[1] / 90 % 4
        i = 0
        while i < n_rotations:
            DIRECTION = d_l[DIRECTION]
            i += 1
    elif instruction[0] == 'R':
        n_rotations = instruction[1] / 90 % 4
        i = 0
        while i < n_rotations:
            DIRECTION = d_r[DIRECTION]
            i += 1

    elif instruction[0] == 'F':
        if DIRECTION == 'N':
            COORD_Y += instruction[1]
        elif DIRECTION == 'S':
            COORD_Y -= instruction[1]
        elif DIRECTION == 'E':
            COORD_X += instruction[1]
        elif DIRECTION == 'W':
            COORD_X -= instruction[1]

print(abs(COORD_X) + abs(COORD_Y))
