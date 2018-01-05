

import numpy as np
import matplotlib.pyplot as plt


def art2mat(art):
    return np.asmatrix([[int(b=='#') for b in list(a)] for a in art.strip().split('/')])


def checkkey(key, pattern):
    if key.shape[0] == pattern.shape[0]:
        for i in range(4):
            key = np.rot90(key)
            if (np.all(key == pattern) or np.all(np.fliplr(key) == pattern) or
            np.all(np.flipud(key) == pattern)):
                return True

    return False


def printart(grid):
    lgrid = grid.tolist()
    signs = {0:'.', 1:'#'}
    art = ''
    for i in range(grid.shape[0]):
        art += ''.join([signs[j] for j in lgrid[i]]) + '\n'

    print(art)


rules = []
with open('021_input.txt','r') as f:
    for line in f:
        words = line.strip().split(' ')
        key = art2mat(words[0])
        val = art2mat(words[2])
        rules.append((key, val))

init = '.#./..#/###'

grid = art2mat(init)
sums = []
for i in range(18):

    gsize = grid.shape[0]
    psize = 2 if gsize % 2 == 0 else 3
    pn = gsize//psize

    for x in range(pn):
        for y in range(pn):
            pattern = grid[x*psize:(x+1)*psize, y*psize:(y+1)*psize]
            new_pattern = None
            for key_, val_ in rules:
                if checkkey(key_, pattern):
                    new_pattern = val_
                    break

            if new_pattern is None:
                print('No pattern found')

            if y == 0:
                new_row = new_pattern.copy()
            else:
                new_row = np.concatenate((new_row, new_pattern), axis=1)

        if x == 0:
            new_grid = new_row.copy()
        else:
            new_grid = np.concatenate((new_grid, new_row), axis=0)

    grid = new_grid
    # printart(grid)
    print(np.sum(grid))
    print(i+1)
    sums.append(np.sum(grid))


print(sums)
# plt.plot(sums)
# plt.show()
