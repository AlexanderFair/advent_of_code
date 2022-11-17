# this is an implementaion of Sanguine Whale's soltuion described here:
# https://www.youtube.com/watch?v=mD-omld3dVQ
letters = 'abcdefg'
def determine_fingerprints(digits):
    fingerprints = []
    for l in letters:
        fingerprint = []
        for digit in digits:
            if l in digit:
                fingerprint.append(str(len(digit)))
        fingerprint.sort()
        fingerprint = "".join(fingerprint)
        fingerprints.append(fingerprint)
    return fingerprints

def determine_fingerprints_in_numbers(digits, fingerprints):
    # finger prints should be in form [a, b, c, etc]
    # for the unshuffled digits, the digit list must be in order - [0, 1, 2, 3, etc]
    # returns a list of lists that are the fingerprints in the i-th number -
    # [fingerprints in 0, fingerprints in 1]

    number_fingerprints = []
    for digit in digits:
        num_fin = []
        for char in digit:
            index = ord(char) - ord('a')
            num_fin.append(fingerprints[index])
        num_fin.sort()
        number_fingerprints.append(num_fin)
    return number_fingerprints

def solve_line(line):
    input_digits, output_digits = line.split(' | ')
    input_digits, output_digits = input_digits.split(), output_digits.split()

    fingerprints = determine_fingerprints(input_digits)
    numbers = determine_fingerprints_in_numbers(input_digits, fingerprints)
    outputs = determine_fingerprints_in_numbers(output_digits, fingerprints)
    # now have a list that is the fingerprints of the segments in each digit,
    # match these up against what the actual digits are
    actual_values = []
    for num in numbers:
        actual_values.append(number_fingerprints.index(num))
    
    # now determine what the output digits by where they are in numbers
    out_num = 0
    for i, out in enumerate(outputs):
        index = numbers.index(out)
        this_actual_digit = actual_values[index]
        # turn this into the 4 digit nubmer its supposed to be - first digit is the thousand digit, then hundreds digit, etc
        out_num += this_actual_digit * (10 ** (3 - i))
    
    return out_num


unshuffled_digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

unshuffled_fingerprints = determine_fingerprints(unshuffled_digits)
number_fingerprints = determine_fingerprints_in_numbers(unshuffled_digits, unshuffled_fingerprints)

total = 0
for line in open('inputs/day8.txt').read().splitlines():
    total += solve_line(line)

print(total)
