
from aoc_016_dance import dance


# Check for a cycle
progs = list(range(16))
progs_start = progs.copy()
for i in range(int(1e9)):
    progs = dance(progs)
    if progs == progs_start:
        break

# Perform dance for 1e9 % cycle times
print(i+1)
for j in range(int(1e9) % (i+1)):
    progs = dance(progs)

final_progs = ''.join([chr(i+97) for i in progs])
print(final_progs)
