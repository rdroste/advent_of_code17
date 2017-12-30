
from knothash import knothash2

key = 'ugkiagan'
dim = 128

result = 0
for row in range(dim):
    this_key = key + '-' + str(row)
    knot_hash = knothash2(this_key)
    # bin_hash = ''.join(''.formatfor(c) for c in list(knot_hash))

    for c in knot_hash:

        scale = 16 ## equals to hexadecimal
        num_of_bits = 4
        this_bin = bin(int(c, scale))[2:].zfill(num_of_bits)
        this_num_bin = [int(b) for b in list(this_bin)]
        result += sum(this_num_bin)

print(result)
