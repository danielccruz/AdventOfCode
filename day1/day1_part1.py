from itertools import combinations

number_list = []

with open('input_file.txt') as input_file:
    for line in input_file.readlines():
        number_list.append(int(line.strip()))

for x in combinations(number_list, 2):
    if x[0]+x[1] == 2020:
        print(x[0]*x[1])


