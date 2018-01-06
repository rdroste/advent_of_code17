
from functools import reduce
from aoc_010_hash import knothash


def knothash2(content):
    lengths = [ord(c) for c in list(content)] + [17, 31, 73, 47, 23]

    sparse = list(range(0,256))
    pos = 0
    skip = 0
    for i in range(64):
        sparse, pos, skip = knothash(lengths, sparse, pos, skip)

    dense = []
    for i in range(0,256,16):
        dense.append(reduce(lambda x,y: x ^ y, sparse[i:i+16]))

    return ''.join('{:02x}'.format(d) for d in dense)


if __name__ == "__main__":
    with open('010_input.txt','r') as f:
        content = f.readline().strip()

    print(knothash2(content))
