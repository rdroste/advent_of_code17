
from aoc_010_hash_2 import knothash2
import numpy as np
from scipy.ndimage.measurements import label

key = 'ugkiagan'
result = 0
bin_list = []
for row in range(128):
    this_key = key + '-' + str(row)
    knot_hash = knothash2(this_key)
    bin_hash = bin(int(knot_hash,16))[2:]
    bin_list += [int(d) for d in list(bin_hash.zfill(128))]

disk = np.asarray(bin_list)
disk = disk.reshape((128,128))

print(label(disk)[1])
