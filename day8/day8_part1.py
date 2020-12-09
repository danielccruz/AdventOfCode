def processor(instructions, position, accumulator, visited_positions):
    if position in visited_positions:
        return accumulator
    if position > len(instructions):
        return accumulator
    if instructions[position][0] == 'jmp':
        visited_positions.append(position)
        position = position + int(instructions[position][1])
        return processor(instructions, position, accumulator, visited_positions)
    elif instructions[position][0] == 'nop':
        visited_positions.append(position)
        return processor(instructions, position + 1, accumulator, visited_positions)
    elif instructions[position][0] == 'acc':
        visited_positions.append(position)
        accumulator = accumulator + int(instructions[position][1])
        return processor(instructions, position + 1, accumulator, visited_positions)


instructions = []
with open('../day8/input_file.txt') as input_file:
    for line in input_file.readlines():
        line = line.strip().split(' ')
        instructions.append(line)

print(processor(instructions, 0, 0, []))
