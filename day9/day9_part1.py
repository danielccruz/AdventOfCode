from itertools import combinations

numbers = [int(line.rstrip('\n')) for line in open('../day9/input_file.txt')]
PREAMBLE_NUMBER = 25

d = {}

for i in range(PREAMBLE_NUMBER, len(numbers)):
    if numbers[i] not in [x + y for x, y in list(combinations(numbers[i - PREAMBLE_NUMBER:i], 2))]:
        print(numbers[i])
        break
