current_mask = 'X' * 36

d = {}


def apply_mask(mask, value):
    for i in range(0, len(value)):
        if mask[i].isdigit():
            value[i] = mask[i]
    return value


for line in open('../day14/input_file.txt').readlines():
    opt, value = line.rstrip().split('=')
    opt = opt.replace(' ', '')
    value = value.replace(' ', '')
    if opt == 'mask':
        current_mask = value
    else:
        opt = opt[4:][:-1]
        d[opt] = apply_mask(current_mask, list(str(bin(int(value))[2:].zfill(36))))

print(sum(map(lambda x: int(''.join(x), 2), [d[key] for key in d.keys()])))
