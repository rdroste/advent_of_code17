

from knothash import knothash
from functools import reduce

with open('010_input.txt','r') as f:
    content = f.readline().strip()
# content = 'AoC 2017'
lengths = [ord(c) for c in list(content)] + [17, 31, 73, 47, 23]

sparse = list(range(0,256))
pos = 0
skip = 0
for i in range(64):
    sparse, pos, skip = knothash(lengths, sparse, pos, skip)

dense = []
for i in range(0,256,16):
    dense.append(reduce(lambda x,y: x ^ y, sparse[i:i+16]))

dense_hash = ''.join('{:02x}'.format(d) for d in dense)

print(dense_hash)
