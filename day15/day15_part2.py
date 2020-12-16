numbers = list(map(int, [(line.rstrip('\n').split(',')) for line in open('../day15/input_file.txt')][0]))

ROUNDS = 30000001

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, value):
        if len(self.stack) == 2:
            self.stack = [value] + [self.stack[0]]
        else:
            self.stack = [value] + self.stack

    def get_last_insert(self):
        return self.stack[0]

    def __str__(self):
        return [x for x in self.stack]

    def __repr__(self):
        return str([x for x in self.stack])


last_spoken_dict = {}

for i in range(0, len(numbers) - 1):
    st = Stack(2)
    st.push(i+1)
    last_spoken_dict[numbers[i]] = st

last_spoken_number = numbers[len(numbers) - 1]


def subtract_last2(values: Stack) -> int:
    if len(values.stack) > 1:
        return values.stack[0] - values.stack[1]
    return values.stack[0]


for i in range(len(numbers) + 1, ROUNDS):
    if last_spoken_number not in last_spoken_dict.keys():
        st = Stack(2)
        st.push(i-1)
        last_spoken_dict[last_spoken_number] = st
        last_spoken_number = 0
    else:
        last_spoken_dict[last_spoken_number].push(i - 1)
        last_spoken_number = subtract_last2(last_spoken_dict[last_spoken_number])

print(last_spoken_number)
