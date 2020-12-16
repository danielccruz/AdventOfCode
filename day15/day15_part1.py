numbers = list(map(int, [(line.rstrip('\n').split(',')) for line in open('../day15/input_file.txt')][0]))

ROUNDS = 2021

last_spoken_dict = {}

for i in range(0, len(numbers) - 1):
    last_spoken_dict[numbers[i]] = [i +1]


last_spoken_number = numbers[len(numbers) - 1]


def subtract_last2(values: list) -> int:
    if len(values) > 1:
        return values[0] - values[1]
    return values[0]


for i in range(len(numbers) + 1, ROUNDS):
    if last_spoken_number not in last_spoken_dict.keys():
        last_spoken_dict[last_spoken_number] = [i-1]
        last_spoken_number = 0
    else:
        last_spoken_dict[last_spoken_number] = [i-1] + last_spoken_dict[last_spoken_number]

        last_spoken_number = subtract_last2(last_spoken_dict[last_spoken_number])

print(last_spoken_number)
