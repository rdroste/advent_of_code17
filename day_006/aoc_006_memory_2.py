
import csv
import numpy as np


def myhash(x):
    return hash(tuple(x))


with open('006_input.txt','r') as infile:
    reader = csv.reader(infile, delimiter='\t')
    line = next(reader)
    mem = np.array(line).astype(np.int)

hashes = [myhash(mem)]
counter = 0
outer_count = 0
while True:
    counter += 1

    pos = np.argmax(mem)
    val = mem[pos]
    mem[pos] = 0

    for i in range(val):
        mem[(pos + 1 + i) % len(mem)] += 1

    this_hash = myhash(mem)
    if outer_count == 0:
        if this_hash in hashes:
            outer_count += 1
            counter = 0
            final_hash = this_hash
        else:
            hashes.append(this_hash)
    else:
        if this_hash == final_hash:
            break


print(counter)
