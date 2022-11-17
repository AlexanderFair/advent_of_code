class Point:
    def __init__(self, l):
        self.x = int(l[0])
        self.y = int(l[1])

    def __repr__(self) -> str:
        return str(self.x) + ',' + str(self.y)


class Line:
    def __init__(self, s):
        self.p1, self.p2 = [Point(x.split(',')) for x in s.split(' -> ')]

    def __repr__(self) -> str:
        return str(self.p1) + ' -> ' + str(self.p2)

    def biggest_x(self):
        return max(self.p1.x, self.p2.x)
    
    def smallest_x(self):
        return min(self.p1.x, self.p2.x)

    def biggest_y(self):
        return max(self.p1.y, self.p2.y)

    def is_vertical(self):
        return self.p1.x == self.p2.x

    def is_horizontal(self):
        return self.p1.y == self.p2.y

    def swap_so_smallest_x_is_p1(self):
        if self.p1.x > self.p2.x:
            self.p1, self.p2 = self.p2, self.p1

    def points_up(self):
        return self.p1.y > self.p2.y

    def covers_vertical(self):
        l = []
        for i in range(min(self.p1.y, self.p2.y), self.biggest_y() + 1):
            l.append(Point([self.p1.x, i]))
        return l

    def covers_horizontal(self):
        l = []
        for i in range(min(self.p1.x, self.p2.x), self.biggest_x() + 1):
            l.append(Point([i, self.p1.y]))
        return l

    def covers(self):
        if self.is_vertical():
            return self.covers_vertical()
        elif self.is_horizontal():
            return self.covers_horizontal()
        
        # is a diagonal line
        l = []
        direction = 1

        self.swap_so_smallest_x_is_p1()
        if self.points_up():
            direction = -1

        for diff in range(0, self.p2.x - self.p1.x + 1):
            l.append(Point([self.p1.x + diff, self.p1.y + diff * direction]))

        return l


lines = open('inputs/day5.txt').read().splitlines()
covered = {}
for i, line in enumerate(lines):
    lines[i] = Line(line)

for line in lines:
    for p in line.covers():
        covered[str(p)] = covered.get(str(p), 0) + 1

print(len([x for x in covered.values() if x > 1]))