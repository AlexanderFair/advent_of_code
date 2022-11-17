class Point:
    max_x = 0
    max_y = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_neighbors(self):
        ns = []
        if self.x > 0:
            ns.append(Point(self.x - 1, self.y))
        if self.y > 0:
            ns.append(Point(self.x, self.y - 1))
        if self.x < Point.max_x:
            ns.append(Point(self.x + 1, self.y))
        if self.y < Point.max_y:
            ns.append(Point(self.x, self.y + 1))
        return ns
    
    def __repr__(self) -> str:
        return str(self.x) + ',' + str(self.y)

    def val_at(g, p):
        return g[p.y][p.x]
    
    def set_true(g, p):
        g[p.y][p.x] = True

class Top3:
    def __init__(self) -> None:
        self.l = []
        pass

    def add(self, x):
        self.l.append(x)
        if len(self.l) > 3:
            self.l.sort()
            self.l.pop(0)
    
    def top_three_product(self):
        return self.l[0] * self.l[1] * self.l[2]


def p(g, x, y):
    print()
    if y > 0:
        if x > 0:
            print('  ', end='')
        print(g[y - 1][x], ' ')
    if x > 0:
        print(g[y][x - 1], end=' ')
    print(g[y][x], end=' ')
    if x < len(g[y]) - 1:
        print(g[y][x + 1], end='')
    print()
    if y < len(grid) - 1:
        if x > 0:
            print('  ', end='')
        print(g[y + 1][x], ' ')
    print()

def pg(g):
    for a in g:
        for x in a:
            if x:
                print('#', end = '')
            else:
                print('.', end='')
        print()
    


grid = open('inputs/day9.txt').read().splitlines()
for i in range(len(grid)):
    grid[i] = [int(x) for x in list(grid[i])]

risk_level_sum = 0
for y in range(len(grid)):
    for x, val in enumerate(grid[y]):
        # check each direction
        if y != 0 and grid[y - 1][x] <= val:
            continue
        if x != 0 and grid[y][x - 1] <= val:
            continue
        if y != len(grid) - 1 and grid[y + 1][x] <= val:
            continue
        if x != len(grid[y]) - 1 and grid[y][x + 1] <= val:
            continue
        # p(grid, x, y)
        risk_level_sum += val + 1

print(risk_level_sum)
# 1901 is too high

# part 2
Point.max_y = len(grid) - 1
Point.max_x = len(grid[0]) - 1
basin_sizes = Top3()
used = [[False] * len(grid[y]) for y in range(len(grid))]
for y in range(len(grid)):
    for x, val in enumerate(grid[y]):
        # if has already been checked
        if Point.val_at(used, Point(x, y)):
            continue
        # check each direction
        if y != 0 and grid[y - 1][x] <= val:
            continue
        if x != 0 and grid[y][x - 1] <= val:
            continue
        if y != len(grid) - 1 and grid[y + 1][x] <= val:
            continue
        if x != len(grid[y]) - 1 and grid[y][x + 1] <= val:
            continue

        # is a low point, and therefore a basin, determine the size 
        size = 0
        open_nodes = [Point(x, y)]
        Point.set_true(used, open_nodes[0])
        while len(open_nodes) != 0:
            # print(open_nodes)
            size += 1
            current = open_nodes.pop()
            neighbours = current.get_neighbors()
            for neighbour in neighbours:
                if Point.val_at(grid, neighbour) == 9:
                    continue

                if not Point.val_at(used, neighbour):
                    open_nodes.append(neighbour)
                    Point.set_true(used, neighbour)
        # pg(used)
        # print(size)
        basin_sizes.add(size)

pg(used)
print(basin_sizes.top_three_product())