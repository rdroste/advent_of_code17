
import math
from itertools import product, starmap


def getcoord(n):
    l = math.ceil((math.sqrt(n)-1)/2)
    ns = 2*l
    rn = n - (2*l-1)**2

    if rn >= 3*ns:
        col = rn - 3*ns - l
        row = -l
    elif rn > 2*ns:
        col = -l
        row = 2*ns - rn + l
    elif rn >= ns:
        col = ns - rn + l
        row = l
    else:
        col = l
        row = rn - l

    return (row, col)


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
