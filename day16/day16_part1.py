import re

rules = {}
i = 0
fp = open('../day16/input_file.txt')


def create_tuples(values: list) -> list:
    l = []
    for i in range(0, len(values), 2):
        l.append((int(values[i]), int(values[i + 1])))
    return l


def tuple_contains(values: list, value: int) -> bool:
    for t in values:
        if value >= t[0] and value <= t[1]:
            return True
    return False


# Reading rules
aux = fp.readline().strip()
while aux != '':
    rules[i] = (create_tuples(re.findall(r'\d+', aux)))
    aux = fp.readline().strip()
    i += 1

# Reading your ticket
aux = fp.readline().strip()
while aux != '':
    aux = fp.readline().strip()

# To simplify, lets flatten the rules dictionary
simple_rule_list = []
for rule in rules.values():
    for v in rule:
        simple_rule_list.append(v)

accum_sum = 0
# Reading nearby tickets
fp.readline().strip()  # Ignoring the line "nearby tickets:"
aux = fp.readline().strip()
while aux != '':
    for v in aux.split(','):
        v = int(v)
        if not tuple_contains(simple_rule_list, v):
            accum_sum += v
    aux = fp.readline().strip()

print(accum_sum)
