
with open('002_input.txt') as f:
    checksum = 0
    for line in f:
        row = list(map(int,line.split('\t')))
        for i, d1 in enumerate(row[:-1]):
            for d2 in row[i+1:]:
                if (max([d1, d2]) / min([d1, d2])) % 1 == 0:
                    checksum += max([d1, d2]) / min([d1, d2])

print(int(checksum))
