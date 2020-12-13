import sys

import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

logger = logging.getLogger('day12')
logger.setLevel(logging.DEBUG)

instructions = [line.rstrip('\n') for line in open('../day12/input_file.txt')]

normalized_instructions = []
for instruction in instructions:
    normalized_instructions.append((instruction[0:1], int(instruction[1:])))

SHIP_COORD_X = 0
SHIP_COORD_Y = 0

WAYPOINT_COORD_X = 10
WAYPOINT_COORD_Y = 1

d_r = {0: (1, 1), 1: (-1, 1), 2: (-1, -1), 3: (1, -1)}
d_l = {0: (1, 1), 1: (1, -1), 2: (-1, -1), 3: (-1, 1)}

for instruction in normalized_instructions:
    logger.debug('----------------' + str(instruction) + '-----------------------')
    if instruction[0] == 'N':
        WAYPOINT_COORD_Y += instruction[1]
    elif instruction[0] == 'S':
        WAYPOINT_COORD_Y -= instruction[1]
    elif instruction[0] == 'E':
        WAYPOINT_COORD_X += instruction[1]
    elif instruction[0] == 'W':
        WAYPOINT_COORD_X -= instruction[1]
    elif instruction[0] == 'L':
        logger.debug(f'Rotating waypoint COUNTER clockwise {instruction[1]} degrees.')
        logger.debug(f'Current ship postion E_{SHIP_COORD_X}, N_{SHIP_COORD_Y}.')

        a, b = d_l[int(instruction[1] / 90 % 4)]
        if int(instruction[1] / 90) == 2:
            WAYPOINT_COORD_X *= a
            WAYPOINT_COORD_Y *= b
        else:
            WAYPOINT_COORD_X *= a
            WAYPOINT_COORD_Y *= b
            aux = WAYPOINT_COORD_Y
            WAYPOINT_COORD_Y = WAYPOINT_COORD_X
            WAYPOINT_COORD_X = aux
        logger.debug(f'Waypoint rotated to E_{WAYPOINT_COORD_X}, N_{WAYPOINT_COORD_Y}.')
    elif instruction[0] == 'R':
        logger.debug(f'Rotating waypoint clockwise{instruction[1]} degrees.')
        logger.debug(f'Current ship postion E_{SHIP_COORD_X}, N_{SHIP_COORD_Y}.')

        a, b = d_r[int(instruction[1] / 90 % 4)]
        if int(instruction[1] / 90) == 2:
            WAYPOINT_COORD_X *= a
            WAYPOINT_COORD_Y *= b
        else:
            WAYPOINT_COORD_X *= a
            WAYPOINT_COORD_Y *= b
            aux = WAYPOINT_COORD_Y
            WAYPOINT_COORD_Y = WAYPOINT_COORD_X
            WAYPOINT_COORD_X = aux
        logger.debug(f'Waypoint rotated to E_{WAYPOINT_COORD_X}, N_{WAYPOINT_COORD_Y}.')

    elif instruction[0] == 'F':
        logger.debug(f'Moving foward {instruction[1]} times.')
        logger.debug(f'Current ship postion E_{SHIP_COORD_X}, N_{SHIP_COORD_Y}.')
        logger.debug(f'Current waypoint postion E_{WAYPOINT_COORD_X}, N_{WAYPOINT_COORD_Y}.')
        logger.debug(
            f'Amount to move east is {instruction[1] * WAYPOINT_COORD_X} and amount to move north is {instruction[1] * WAYPOINT_COORD_Y}.')
        SHIP_COORD_X += (instruction[1] * WAYPOINT_COORD_X)
        SHIP_COORD_Y += (instruction[1] * WAYPOINT_COORD_Y)
        logger.debug(f'Moved ship postion to E_{SHIP_COORD_X}, N_{SHIP_COORD_Y}.')

print(abs(SHIP_COORD_X) + abs(SHIP_COORD_Y))
