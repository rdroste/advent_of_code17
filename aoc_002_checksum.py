
with open('002_input.txt') as f:
    checksum = 0
    for line in f:
        row = list(map(int,line.split('\t')))
        checksum += max(row)-min(row)

print(checksum)
