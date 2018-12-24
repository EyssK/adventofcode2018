from itertools import combinations, product
import re

with open("Day3input.txt") as file:
    lines = file.read().splitlines()

s = dict()
pattern = re.compile(r".* @ (\d+),(\d+): (\d+)x(\d+)")
for a in lines:
    x, y, l, L = pattern.match(a).group(1, 2, 3, 4)
    x, y, l, L = int(x), int(y), int(l), int(L)
    for (r, t) in product(range(x, x + l), range(y, y + L)):
        s[(r, t)] = s.setdefault((r, t), 0) + 1

print("part1 =", len([x for x in s.values() if x > 1]))

for a in lines:
    x, y, l, L = pattern.match(a).group(1, 2, 3, 4)
    x, y, l, L = int(x), int(y), int(l), int(L)
    for (r, t) in product(range(x, x + l), range(y, y + L)):
        if s[(r, t)] > 1:
            break
    else:
        print("part2 =", a[1:5])