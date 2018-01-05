
import numpy as np


def art2mat(art):
    return np.asmatrix([[int(b=='#') for b in list(a)] for a in art.strip().split('/')])


def mat2tuple(mat):
    return tuple(np.asarray(mat.flatten()).tolist()[0])


rules = {}
with open('021_input.txt','r') as f:
    for line in f:
        words = line.strip().split(' ')
        key = art2mat(words[0])
        val = art2mat(words[2])
        for i in range(4):
            key = np.rot90(key)
            rules[mat2tuple(key)] = val
            rules[mat2tuple(np.fliplr(key))] = val
            rules[mat2tuple(np.flipud(key))] = val

init = '.#./..#/###'

grid = art2mat(init)
for i in range(18):

    gsize = grid.shape[0]
    psize = 2 if gsize % 2 == 0 else 3
    pn = gsize//psize

    for x in range(pn):
        for y in range(pn):
            pattern = grid[x*psize:(x+1)*psize, y*psize:(y+1)*psize]
            new_pattern = rules[mat2tuple(pattern)]

            if y == 0:
                new_row = new_pattern.copy()
            else:
                new_row = np.concatenate((new_row, new_pattern), axis=1)

        if x == 0:
            new_grid = new_row.copy()
        else:
            new_grid = np.concatenate((new_grid, new_row), axis=0)

    grid = new_grid
    if i == 4:
        print(np.sum(grid))

print(np.sum(grid))
