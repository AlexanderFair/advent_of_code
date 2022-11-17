d = {}
for x in [int(z) for z in open('inputs\day6.txt').read().split(',')]:
    d[x] = d.get(x, 0) + 1

days = 256

for _ in range(days):
    nd = {}
    for key in d.keys():
        if key == 0:
            nd[8] = d[key]
            nd[6] = nd.get(6, 0) + d[key]
        else:
            nd[key - 1] = nd.get(key - 1, 0) + d[key]
    d = nd


count = sum(d.values())
print(count)