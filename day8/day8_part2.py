def processor(instructions, position, accumulator, visited_positions):
    if position in visited_positions:
        return -1
    if position > len(instructions):
        return accumulator
    if instructions[position][0] == 'jmp':
        visited_positions.append(position)
        position = position + int(instructions[position][1])
        return processor(instructions, position, accumulator, visited_positions)
    if instructions[position][0] == 'nop':
        visited_positions.append(position)
        return processor(instructions, position + 1, accumulator, visited_positions)
    if instructions[position][0] == 'acc':
        visited_positions.append(position)
        accumulator = accumulator + int(instructions[position][1])
        return processor(instructions, position + 1, accumulator, visited_positions)
    return accumulator


instructions = [line.rstrip('\n').split(' ') for line in open('input_file.txt')]

###########################
BRUTE_FORCE_SOLUTION = True
###########################


for instruction_i in range(0, len(instructions)):
    result = processor(instructions, 0, 0, [])
    if result == -1:
        if instructions[instruction_i][0] == 'nop':
            instructions[instruction_i][0] = 'jmp'
            result = processor(instructions, 0, 0, [])
            if result == -1:
                instructions[instruction_i][0] = 'nop'
            else:
                print('Bug found on position: {}. Accumulator value is {}.'.format(instruction_i, result))
                break
        elif instructions[instruction_i][0] == 'jmp':
            instructions[instruction_i][0] = 'nop'
            result = processor(instructions, 0, 0, [])
            if result == -1:
                instructions[instruction_i][0] = 'jmp'
            else:
                print('Bug found on position: {}. Accumulator value is {}.'.format(instruction_i, result))
                break
