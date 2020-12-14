current_mask = 'X' * 36

d = {}


def apply_mask(mask, value) -> list:
    for i in range(0, len(value)):
        if mask[i] in ['1', 'X']:
            value[i] = mask[i]
    return value


def generate_floaters(value: str) -> list:
    if value.isdigit():
        return [value]
    for i in range(0, len(value)):
        if value[i] == 'X':
            return generate_floaters(value[0:i] + '0' + value[i + 1:]) + \
                   generate_floaters(value[0:i] + '1' + value[i + 1:])
    return []


for line in open('../day14/input_file.txt').readlines():
    opt, value = line.rstrip().split('=')
    opt = opt.replace(' ', '')
    value = value.replace(' ', '')
    if opt == 'mask':
        current_mask = value
    else:
        opt = opt[4:][:-1]
        for floater in generate_floaters(''.join(apply_mask(current_mask, list(str(bin(int(opt))[2:].zfill(36)))))):
            d[int(floater, 2)] = value
print(sum(map(int, d.values())))
