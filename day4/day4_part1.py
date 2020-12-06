passports = []
aux = []
# ADD 2 NEWLINES TO THE INPUT FILE.
with open('input_file.txt') as input_file:
    for line in input_file.readlines():
        aux.append(line.strip())
        if line == '\n':
            passports.append(' '.join(aux))
            aux = []

# Processing
processed_passports = {}
validated_passports = 0
for passport in passports:
    interm = list(filter(lambda a: a != '', passport.split(' ')))
    for field in interm:
        x = field.split(':')
        processed_passports[x[0]] = x[1]
    check = all(i in list(processed_passports.keys()) for i in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    if check:
        validated_passports = validated_passports + 1
    processed_passports.clear()

print(validated_passports)
