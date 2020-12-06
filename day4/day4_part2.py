passports = []
aux = []

def split(word):
    return [char for char in word]

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
        if 1920 <= int(processed_passports['byr']) <= 2002 and \
                2010 <= int(processed_passports['iyr']) <= 2020 <= int(processed_passports['eyr']) <= 2030 and \
                processed_passports['ecl'] in ['amb', 'blu', 'brn', 'gry', 'hzl', 'oth', 'grn'] and \
                len(processed_passports['pid']) == 9 and \
                processed_passports['pid'].isdigit():
            if processed_passports['hgt'].endswith('cm') and (150 <= int(processed_passports['hgt'][:-2]) <= 193):
                if processed_passports['hcl'].startswith('#') and len(processed_passports['hcl']) == 7:
                    check2 = all(jj in split('0123456789abcdef') for jj in split(processed_passports['hcl'][1:]) )
                    if check2:
                        validated_passports = validated_passports + 1
                        pass
            if processed_passports['hgt'].endswith('in') and (59 <= int(processed_passports['hgt'][:-2]) <= 76):
                if processed_passports['hcl'].startswith('#') and len(processed_passports['hcl']) == 7:
                    check2 = all(j in split('0123456789abcdef') for j in split(processed_passports['hcl'][1:]))
                    if check2:
                        validated_passports = validated_passports + 1

    processed_passports.clear()

print(validated_passports)
