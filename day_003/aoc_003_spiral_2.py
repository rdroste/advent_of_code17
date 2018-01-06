
from itertools import product, starmap
from aoc_003_spiral import getcoord


def getneighbours(pos):
    x, y = pos
    return list(starmap(lambda a,b: (x+a, y+b), list(product((0,-1,+1), (0,-1,+1)))))[1:]


limit = 368078

i = 2
spiral = {(0,0):1}
while True:

    pos = getcoord(i)
    neighbours = getneighbours(pos)

    x = 0
    for n in neighbours:
        if n in spiral:
            x += spiral[n]

    if x > limit:
        break

    spiral[pos] = x
    i += 1

print(x)
