
"""
def fun():
    with open("Day5input.txt") as file:
        poly = file.read().strip()
        # poly = "dabAcCaCBAcCcaDA"
        short = list(poly)
        while True:
            for i, (a, b) in enumerate(zip(short[:len(short)-1], short[1:len(short)])):
                if a.swapcase() == b:
                    short.pop(i)
                    short.pop(i)
                    break
            else:
                break
        print("Part1 :", len(short))


fun()

"""

from string import *


def collapse(s):
    p = ['.']
    for u in s:
        v = p[-1]
        if v != u and v.lower() == u.lower():
            p.pop()
        else:
            p.append(u)
        #print(v,u,p)
    return len(p) - 1


s = open('Day5input.txt').read().strip()
collapse("dabAcCaCBAcCcaDA")
#quit()
print(collapse(s))
print(min(collapse(c for c in s if c.lower() != x) for x in ascii_lowercase))
