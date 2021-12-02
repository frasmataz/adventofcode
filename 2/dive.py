lines = []

with open('data.txt', 'r') as text_file:
    lines = text_file.read().split('\n')

# PART 1
# Plot course

depth = 0
horiz = 0

for line in lines:
    sp = line.split(' ')
    direction = sp[0]
    magnitude = int(sp[1])

    if direction == 'forward':
        horiz = horiz + magnitude
    elif direction == 'down':
        depth = depth + magnitude
    elif direction == 'up':
        depth = depth - magnitude

print(f'Horizontal position: {horiz}, Depth: {depth}')


# PART 2
# Plot course with aim

aim = 0
depth = 0
horiz = 0

for line in lines:
    sp = line.split(' ')
    direction = sp[0]
    magnitude = int(sp[1])

    if direction == 'forward':
        horiz = horiz + magnitude
        depth = depth + (aim * magnitude)
    elif direction == 'down':
        aim = aim + magnitude
    elif direction == 'up':
        aim = aim - magnitude

print(f'Horizontal position: {horiz}, Depth: {depth}')