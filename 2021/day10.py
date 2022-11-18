openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']

def open_to_close(opener):
    return closers[openers.index(opener)]

def corresponds(o, c):
    return openers.index(o) == closers.index(c)


# combined parts if just get rid of the last return pretty much just does part 1
def error(s):
    expected = []
    for c in s:
        if c in openers:
            expected.append(c)
        else:
            # this is a closing
            # if this correctly closes a chunk
            if corresponds(expected[-1], c):
                expected.pop()
            else:
                # this is a syntax error!
                return c
    
    # return the list that should be at the end the string,
    # which is the closer versions of the reversed expected list
    return [open_to_close(c) for c in expected][::-1]


def score_completion(s):
    score = 0
    for c in s:
        score *= 5
        score += closers.index(c) + 1
    return score



lines = open('2021/inputs/day10.txt').read().splitlines()
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
counts = {')': 0, ']': 0, '}': 0, '>': 0}
part_two_scores = []
for line in lines:
    e = error(line)
    if type(e) == str:
        counts[error(line)] += 1
        continue

    part_two_scores.append(score_completion(e))


print('part one:', sum([scores[x] * counts[x] for x in counts.keys()]))
part_two_scores.sort()
print('part two:', part_two_scores[len(part_two_scores) // 2])
