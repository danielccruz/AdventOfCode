notes = [line.rstrip('\n') for line in open('../day13/input_file.txt')]

bus_ids = [x for x in notes[1].split(',')]


##### This was my solution. It ran for 4 hours but it didn't find anything.
##### Some bird talked about Chinese Remainder Theorem so I tried co create a solution with it.


# time = 100000000000000
# increment = 1
# while True:
#     if time % int(bus_ids[0]) == 0:
#         for i in range(1, len(bus_ids)):
#             if bus_ids[i] == 'x':
#                 continue
#             else:
#                 if (time + i) % int(bus_ids[i]) == 0:
#                     if i == len(bus_ids) - 1:
#                         print(time)
#                         exit()
#                 else:
#                     increment = int(bus_ids[0])
#                     break
#     time += increment

# This only works since the input numbers are relatively prime







import math
### Auxiliary functions ###
# Congruence solving


def extended_euclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def invert_modulo(a, n):
    (b, x) = extended_euclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b



# Multiply all the elements of the list except the exception
def custom_mult(numbers: list, exception: int):
    if numbers == []:
        return 1
    if numbers[0] == exception:
        return custom_mult(numbers[1::], exception)
    return numbers[0] * custom_mult(numbers[1::], exception)


def construct_CRT_table(numbers: [tuple]) -> int:
    # Get list of the remainders and modulos
    remainders = [n[0] for n in numbers]
    modulos = [n[1] for n in numbers]
    totals = 0
    for i in range(0, len(numbers)):
        n_i = custom_mult(modulos, modulos[i])
        inv_mod_i = invert_modulo(n_i, modulos[i])
        bNx_i = remainders[i] * n_i * inv_mod_i
        #print(f'b_{i} = {remainders[i]} || N_{i} = {n_i} || x_{i} = {inv_mod_i} || b_N_x_{i} = {bNx_i}')
        totals += bNx_i
    return math.prod(modulos) - (totals % math.prod(modulos))

def prepate_input():
    processed_list = []
    for i in range(0, len(bus_ids)):
        if bus_ids[i].isdigit():
            processed_list.append((i+1, int(bus_ids[i])))
    return processed_list

print(construct_CRT_table(prepate_input()) + 1)
