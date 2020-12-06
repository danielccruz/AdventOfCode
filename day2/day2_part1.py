from itertools import combinations

passwords = []

with open('input_file.txt') as input_file:
    for line in input_file.readlines():
        passwords.append(line.strip().split(' '))

validPWDs = 0
for pwd in passwords:
    tuple_min_max = pwd[0].split('-')
    target_letter = pwd[1][:-1]

    num_occurs = pwd[2].count(target_letter)

    if int(tuple_min_max[0]) <= num_occurs <= int(tuple_min_max[1]):
        validPWDs = validPWDs + 1

print(validPWDs)