def part1():
    lines = [int(x) for x in open('inputs/day1.txt').read().splitlines()]

    count = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i - 1]:
            count += 1

    print(count)

def part2():
    lines = [int(x) for x in open('inputs/day1.txt').read().splitlines()]

    count = 0
    for i in range(len(lines) - 3):
        if lines[i] < lines[i + 3]:
            count += 1

    print(count)


part2()