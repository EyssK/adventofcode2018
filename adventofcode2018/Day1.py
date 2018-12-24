from itertools import cycle

acc = 0
known = {}
part1found = False
with open("Day1input.txt") as file:
    lines = file.read().splitlines()

for line in cycle(lines):
    if line[0] == '-':
        acc -= int(line[1:])
    else:
        acc += int(line[1:])

    if acc in known:
        print("part2 = " + str(acc))
        quit(0)
    else:
        known[acc] = True

    if not part1found and lines.index(line) == (len(lines)-1):
        part1found = True
        print("part1 = " + str(acc))
