def calc_row_position(code, interval):
    if code == '':
        return int(interval[0])
    if code[0] == 'F':
        new = (interval[1] - interval[0] + 1) / 2
        return calc_row_position(code[1:], [interval[0], interval[1] - new])
    if code[0] == 'B':
        new = (interval[1] - interval[0] + 1) / 2
        return  calc_row_position(code[1:], [interval[0] + new, interval[1]])

def calc_seat(code, interval):
    if code == '':
        return int(interval[0])
    if code[0] == 'L':
        new = (interval[1] - interval[0] + 1) / 2
        return calc_seat(code[1:], [interval[0], interval[1] - new])
    if code[0] == 'R':
        new = (interval[1] - interval[0] + 1) / 2
        return  calc_seat(code[1:], [interval[0] + new, interval[1]])


max_value = 0
with open('input_file.txt') as input_file:
   for line in input_file.readlines():
       line = line.strip()
       val = calc_row_position(line[:7], [0,127])* 8 + calc_seat(line[7:], [0,7])
       if val>max_value:
           max_value = val
print(max_value)
