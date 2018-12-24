from itertools import combinations

with open("Day2input.txt") as file:
    lines = file.read().splitlines()

nb2 = 0
nb3 = 0
for line in lines:
    s = {}.fromkeys(line, 0)
    for c in line:
        s[c] += 1
    for c in s:
        if s[c] == 2:
            nb2 += 1
            break
    for c in s:
        if s[c] == 3:
            nb3 += 1
            break

print("part1 = " + str(nb2 * nb3))

for (a, b) in combinations(lines, 2):
    for c in range(1, len(a)-1):
        if (a[:c] == b[:c]) and (a[c+1:] == b[c+1:]):
            print("part2 =", a[:c] + a[c+1:])
            quit(0)
