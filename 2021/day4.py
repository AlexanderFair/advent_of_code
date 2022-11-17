lines = open('inputs/day4.txt').read().splitlines()

nums = [int(x) for x in lines[0].split(',')]

# determine when each number is pulled (loop going down as im not sure if a number can be pulled multiple times, and this will get the earliest pull)
turnnum = {}
for i in range(len(nums) - 1, -1, -1):
    turnnum[nums[i]] = i


# pretty much what mincols is
# for j in range(5):
#     col = [row[j] for row in board]

boards = []
winturns = []

i = 2
while i < len(lines):
    board = []
    tboard = []
    for j in range(5):
        board.append([turnnum[int(x)] for x in lines[i + j].split()])
        tboard.append([turnnum[int(x)] for x in lines[i + j].split()])
    
    boards.append(tboard)

    # find the turnnum on which this board will win
    minrows = min([max(row) for row in board])
    mincols = min([max([row[j] for row in board]) for j in range(5)])
    winturns.append(min(minrows, mincols))

    i += 6

# calculate score
turn = min(winturns)
winneri = winturns.index(turn)

sum_of_unmarked = 0

for row in boards[winneri]:
    for x in row:
        if x > turn:
            # is an unmarked number
            sum_of_unmarked += nums[x]

print(sum_of_unmarked * nums[turn])

# for part two, the only change is maxing instead of minning the winturns\
turn = max(winturns)
winneri = winturns.index(turn)

sum_of_unmarked = 0

for row in boards[winneri]:
    for x in row:
        if x > turn:
            # is an unmarked number
            sum_of_unmarked += nums[x]

print(sum_of_unmarked * nums[turn])