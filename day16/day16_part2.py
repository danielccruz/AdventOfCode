import re

rules = {}
rules_map = {}
i = 0
fp = open('../day16/input_file.txt')


def create_tuples(values: list) -> list:
    l = []
    for i in range(0, len(values), 2):
        l.append((int(values[i]), int(values[i + 1])))
    return l


def get_bool(boolean_list: list) -> bool:
    if not boolean_list:
        return True
    if not boolean_list[0]:
        return False
    return get_bool(boolean_list[1::])


def tuple_contains(values: list, value: int) -> bool:
    for t in values:
        if t[0] <= value <= t[1]:
            return True
    return False


def get_possible_indexes(values: list, rules: dict) -> list:
    possible_indexes = []
    for v in values:
        y = []
        for k in rules.keys():
            if tuple_contains(rules[k], v):
                y.append(k)
        possible_indexes.append(y)
    return list(set.intersection(*map(set, possible_indexes)))


# Reading rules
aux = fp.readline().strip()
while aux != '':
    rules_map[i] = aux.split(':')[0]
    rules[i] = create_tuples(re.findall(r'\d+', aux))
    aux = fp.readline().strip()
    i += 1

# Reading your ticket
aux = fp.readline().strip()
my_ticket = []
while aux != '':
    my_ticket = aux.split(',')
    aux = fp.readline().strip()

my_ticket = list(map(int, my_ticket))

# To simplify, lets flatten the rules dictionary
simple_rule_list = []
for rule in rules.values():
    for v in rule:
        simple_rule_list.append(v)

# Reading nearby tickets
fp.readline().strip()  # Ignoring the line "nearby tickets:"
aux = fp.readline().strip()

valid_tickets = []
while aux != '':
    if get_bool([tuple_contains(simple_rule_list, int(v)) for v in aux.split(',')]):
        valid_tickets.append(list(map(int, aux.split(','))))
    aux = fp.readline().strip()

###  HARD PART ###

# Get possible fields for each index
# Transpose valid tickets
valid_tickets = list(map(list, zip(*valid_tickets)))

final_list = []
# For each column of the valid tickets create a list of possible fields it can take
for i in range(0, len(valid_tickets)):
    final_list.append(get_possible_indexes(valid_tickets[i], rules))

# ITS BRUTE FORCE TIME!

# Save order for later
array_order = range(0, len(final_list))
array_order = [x for (y, x) in sorted(zip(final_list, array_order), key=lambda pair: len(pair[0]))]

final_list.sort(key=len)


#### So, at this point I check the output of `final_list` and the list have increasing size (1,2,3,4...) so
#### the algo will simply be iterate and remove all the occurences from the other lists

def value_remover(value: int, values: list) -> list:
    new_list = []
    for l in values:
        new_list.append(list(filter(lambda x: x != value, l)))
    return new_list


final_order = []
for i in range(0, len(final_list)):
    final_order.append(final_list[0][0])
    final_list = value_remover(final_list[0][0], final_list[1::])

# Recover the order from before
final_order = [x for (y, x) in sorted(zip(array_order, final_order), key=lambda pair: pair[0])]

# Get the `departure` positions
result = 1
for k in rules_map.keys():
    if rules_map[k].startswith('departure'):
        result *= (my_ticket[final_order.index(k)])
print(result)
