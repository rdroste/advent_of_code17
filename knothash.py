
from functools import reduce


def knothash(lengths, nums, pos, skip):
    n = len(nums)
    for l in lengths:

        if l > n-1:
            continue

        for i in range(0, l//2):
            x = (pos + i) % n
            y = (pos + l - i - 1) % n
            nums[x], nums[y] = nums[y], nums[x]

        pos = (pos + l + skip) % n
        skip += 1

    return nums, pos, skip


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
