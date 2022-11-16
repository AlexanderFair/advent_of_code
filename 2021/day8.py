def single_display_output(line):
    digit_reps, output_digits = line.split(' | ')
    digit_reps, output_digits = digit_reps.split(), output_digits.split()
    all_letters = set('abcdefg')

    # determine what some of the digit_reps are
    seven = ''
    five_segments = []
    six_segments = []
    # disregards eight as it provides no information - 4 too!
    for repr in digit_reps:
        match len(repr):
            case 2:
                one = repr
            case 3:
                seven = repr
            case 5:
                five_segments.append(set(repr))
            case 6:
                six_segments.append(set(repr))

    # determine which is the three
    three = set()
    two_or_five = []
    # convert to sets first
    for i, num in enumerate(five_segments):
        # if the difference to one of the others is 2, then it is not the three
        is_three = True
        for j in range(len(five_segments)):
            if j == i:
                continue
            amount_difference = len(num.difference(five_segments[j]))
            if amount_difference == 2:
                is_three = False
                break
        
        if is_three:
            three = num
        else:
            two_or_five.append(num)

    b_or_e = all_letters.difference(three)

    # determine what is c, d, e from what is missing from 0, 6 and 9
    c_or_d_or_e = set()
    for num in six_segments:
        c_or_d_or_e.update(all_letters.difference(num))

    # know that what is in one is c or f
    c_or_f = set(one)

    actual_values = {}
    # determine 'a' by what is in 7 but not in 1
    for char in seven:
        if char not in c_or_f:
            actual_values[char] = 'a'
            break

    # determine what the ones in c_or_d_or_e are
    for char in c_or_d_or_e:
        if char in c_or_f:
            actual_values[char] = 'c'
            c_or_f.remove(char)
            actual_values[list(c_or_f)[0]] = 'f'
        elif char in b_or_e:
            actual_values[char] = 'e'
            b_or_e.remove(char)
            actual_values[list(b_or_e)[0]] = 'b'
        else:
            actual_values[char] = 'd'
    
    
    # only one left is g
    for char in all_letters:
        if not char in actual_values.keys():
            actual_values[char] = 'g'
            break
    
        
    # determine what the outputs are
    strs_to_nums = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}
    actual_numbers = []
    for digit in output_digits:
        s = [actual_values[c] for c in digit]
        s.sort()
        s = "".join(s)
        actual_numbers.append(strs_to_nums[s])
    
    return actual_numbers[0] * 1000 + actual_numbers[1] * 100 + actual_numbers[2] * 10 + actual_numbers[3]


total = 0
for line in open('inputs/day8.txt').read().splitlines():
    total += single_display_output(line)
print(total)