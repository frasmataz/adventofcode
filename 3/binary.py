import numpy

lines = []

with open('data.txt', 'r') as text_file:
    lines = text_file.read().split('\n')

# PART 1
# Calculate power

def get_totals(array):
    # Create 'totals' array with an integer per column in input words
    # For each column in input words, add 1 to column's total if '1', subtract 1 if '0'
    # Total for each column will be positive if there are more 1s, negative if more 0s.

    totals = numpy.zeros(shape=word_length, dtype=int)

    for line in array:
        for index, digit in enumerate(line):
            if digit == '0':
                totals[index] = totals[index] - 1
            elif digit == '1':
                totals[index] = totals[index] + 1

    return totals

word_length = len(lines[0])

totals = get_totals(lines)

# Check if each column's total is positive or negative
# Build gamma_rate binary word by bit-shifting left and adding 1s/0s
gamma_rate = 0b0

for digit in totals:
    gamma_rate = gamma_rate << 1

    if digit > 0:
        gamma_rate = gamma_rate + 0b1

# Epsilon rate is the inverse of gamma rate
epsilon_rate = gamma_rate ^ (2 ** word_length - 1)

# Multiply together to get power rate
power_rate = gamma_rate * epsilon_rate

print(f'Gamma rate:\t\t{bin(gamma_rate)}')
print(f'Epsilon rate:\t\t{bin(epsilon_rate)}')
print(f'Power rate:\t\t{power_rate}\n')


# PART 2
# Life support

def whittle_array(array, column, most_common):
    # Take input array, word column, and bit criteria.
    # Produce array with ineligible words removed.
    # If only 1 item remains, return it, else recuse on next column.

    totals = get_totals(array)
    output = []
    expected_bit = 1 if totals[column] >= 0 else 0
    expected_bit = expected_bit if most_common else expected_bit ^ 1

    for line in array:
        if line[column] == str(expected_bit):
            output.append(line)

    if len(output) == 1:
        return output[0]
    else:
        return whittle_array(output, column + 1, most_common)

oxy_rating = int(whittle_array(lines, 0, True), 2)
co2_rating = int(whittle_array(lines, 0, False), 2)

print(f'Oxygen rating:\t\t{bin(oxy_rating)}')
print(f'CO2 rating:\t\t{bin(co2_rating)}')
print(f'Life support rating:\t{oxy_rating * co2_rating}')