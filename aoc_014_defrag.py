
from aoc_010_hash_2 import knothash2

key = 'ugkiagan'
result = 0
for row in range(128):
    this_key = key + '-' + str(row)
    knot_hash = knothash2(this_key)
    bin_hash = ''.join('{:04b}'.format(int(k, 16)) for k in knot_hash)
    result += bin_hash.count('1')

print(result)
