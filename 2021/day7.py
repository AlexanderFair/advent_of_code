def part1():
    crabs = [int(x) for x in open('inputs\day7.txt').read().split(',')]

    min_cost = 100000000000000000000
    for target in range(max(crabs) + 1):
        fuel_cost = sum([abs(crab - target) for crab in crabs])
        min_cost = min(min_cost, fuel_cost)

    print(min_cost)

def part2():
    crabs = [int(x) for x in open('inputs\day7.txt').read().split(',')]

    min_cost = 100000000000000000000
    for target in range(max(crabs) + 1):
        fuel_cost = 0
        for crab in crabs:
            dist = abs(crab - target)
            fuel_cost += dist * (dist + 1) // 2
        min_cost = min(min_cost, fuel_cost)

    print(min_cost)

part2()