def part1():
    lines = open('inputs/day3.txt').read().splitlines()

    counts = [0] * len(lines[1])
    for l in lines:
        for i, c in enumerate(l):
            if c == '1':
                counts[i] += 1
                
    gamma = ''
    epsilon = ''
    for c in counts:
        if c > 500:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print(int(gamma, 2) * int(epsilon, 2))


def most_common(arr, i):
    c = [0, 0]
    for l in arr:
        c[int(l[i])] += 1

    if c[0] > c[1]:
        return '0'
    return '1'

def part2():
    ox = open('inputs/day3.txt').read().splitlines()
    co = ox.copy()

    i = 0
    digitCount = len(ox[0])
    while i < digitCount and len(ox) > 1:
        c = most_common(ox, i)
        ox = [x for x in ox if x[i] == c]
        i += 1

    i = 0
    digitCount = len(co[0])
    while i < digitCount and len(co) > 1:
        c = most_common(co, i)
        co = [x for x in co if not x[i] == c]
        i += 1

    print(int(ox[0], 2) * int(co[0], 2))

part2()

    



