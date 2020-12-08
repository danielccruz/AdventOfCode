counter = 0

answers = [line.rstrip('\n') for line in open('input_file.txt')]

aux = []
for answer in answers:
    if answer == '':
        counter += len(set(aux[0]).intersection(*aux))
        aux = []
    else:
        aux.append(answer)

print(counter)