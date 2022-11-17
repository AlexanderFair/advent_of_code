def part1():
    lines = open('inputs/day2.txt').read().splitlines()
    for i, l in enumerate(lines):
        li = l.split(' ')
        lines[i] = [li[0], int(li[1])]


    vals = [0, 0, 0]
    dirs = {'down': 0, 'up': 1, 'forward': 2}
    dir(dirs)

    for l in lines:
        vals[dirs[l[0]]] += l[1]


    print((vals[0] - vals[1]) * vals[2])

def part2():
    lines = open('inputs/day2.txt').read().splitlines()
    for i, l in enumerate(lines):
        li = l.split(' ')
        lines[i] = [li[0], int(li[1])]

    depth = 0
    horizontal = 0
    aim = 0
    for l in lines:
        if l[0] == 'down':
            aim += l[1]
        elif l[0] == 'up':
            aim -= l[1]
        else:
            horizontal += l[1]
            depth += aim * l[1]

    print(horizontal * depth)

part2()