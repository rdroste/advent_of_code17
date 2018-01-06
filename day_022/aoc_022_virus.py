
import numpy as np


moves = {0:(0,-1), 1:(1,1), 2:(0,1), 3:(1,-1)}  # n, w, s, e


def art2mat(art):
    return np.asmatrix([[int(b=='#') for b in list(a)] for a in art.strip().split('/')])


def printmat(grid):
    lgrid = grid.tolist()
    signs = {0:'.', 1:'#'}
    art = ''
    for i in range(grid.shape[0]):
        art += ''.join([signs[j] for j in lgrid[i]]) + '\n'

    print(art)


with open('022_input.txt','r') as f:
    lines = [line.strip() for line in f]

art = '/'.join(lines)
# art = '..#/#../...'

cluster = art2mat(art)

csize = cluster.shape[0]
pos = [csize//2] * 2
direction = 0
infect_count = 0
for b in range(10000):
    if cluster[pos[0],pos[1]]:
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
        infect_count += 1

    cluster[pos[0],pos[1]] = int(not(cluster[pos[0],pos[1]]))

    pos[moves[direction][0]] += moves[direction][1]

    if max(pos) >= csize or min(pos) < 0:
        cluster = np.concatenate((np.zeros_like(cluster[0,:]), cluster, np.zeros_like(cluster[0,:])), axis=0)
        cluster = np.concatenate((np.zeros_like(cluster[:,0]), cluster, np.zeros_like(cluster[:,0])), axis=1)
        # cluster = np.concatenate((np.zeros(csize+2), cluster, np.zeros(csize+2)), axis=1)
        csize += 2
        pos = [p+1 for p in pos]

print(infect_count)
