import csv

with open('002_input.txt') as infile:
    reader = csv.reader(infile, delimiter='\t')
    diffs = []
    for line in reader:
        row = list(map(int,line))
        diffs.append(max(row)-min(row))

print(sum(diffs))
