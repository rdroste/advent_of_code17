
import numpy as np


moves = {0:(0,-1), 1:(1,1), 2:(0,1), 3:(1,-1)}  # n, w, s, e
logic = {0:-1, 1:0, 2:1, 3:2}


def art2mat(art):
    return np.asmatrix([[int(b=='#') for b in list(a)] for a in art.strip().split('/')])


with open('022_input.txt','r') as f:
    lines = [line.strip() for line in f]

art = '/'.join(lines)
# art = '..#/#../...'

cluster = 2*art2mat(art)

csize = cluster.shape[0]
pos = [csize//2] * 2
direction = 0
infect_count = 0
for b in range(10000000):

    if cluster[pos[0],pos[1]] == 1:
        infect_count += 1

    direction = (direction + logic[cluster[pos[0],pos[1]]]) % 4

    cluster[pos[0],pos[1]] = (cluster[pos[0],pos[1]] + 1) % 4

    pos[moves[direction][0]] += moves[direction][1]

    if max(pos) >= csize or min(pos) < 0:
        cluster = np.concatenate((np.zeros_like(cluster[0,:]), cluster, np.zeros_like(cluster[0,:])), axis=0)
        cluster = np.concatenate((np.zeros_like(cluster[:,0]), cluster, np.zeros_like(cluster[:,0])), axis=1)
        csize += 2
        pos = [p+1 for p in pos]

print(infect_count)
