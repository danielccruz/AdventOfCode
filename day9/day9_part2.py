numbers = [int(line.rstrip('\n')) for line in open('../day9/input_file.txt')]
TARGET_NUMBER = 1212510616


def get_list_sum(lst, value, width):
    if value == TARGET_NUMBER:
        return lst[0:width - 1]
    if value > TARGET_NUMBER:
        return -1
    return get_list_sum(lst, sum(lst[0:width]), width + 1)


last_valid_position = 0
target_number_list = []

for i in range(0, len(numbers)):
    result = get_list_sum(numbers[i::], 0, 0)
    if result != -1:
        print(min(result) + max(result))
        break
