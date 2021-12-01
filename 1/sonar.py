from functools import reduce

lines = []

with open('data.txt', 'r') as text_file:
    lines = list(map(int, text_file.read().split('\n')))


# PART 1
# Count increases

count = 0

for i in range(0, len(lines)-1):
    element = lines[i]
    next_element = lines[i+1]

    if element < next_element:
        count = count + 1

print(f'Part 1: Number of single-reading increases: {count}')


# PART 2
# Sliding window

window_size = 3
prev_window_sum = 0
count = 0

for i in range(0, len(lines) - (window_size-1)):
    window = lines[i:i+window_size]
    window_sum = reduce(lambda a, b: a+b, window)

    if prev_window_sum != 0 and window_sum > prev_window_sum:
        count = count + 1

    prev_window_sum = window_sum

print(f'Part 2: Number of sliding-window increases: {count}')