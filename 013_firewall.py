
walls = {}
with open('013_input.txt','r') as f:
    for line in f:
        words = line.split()
        walls[int(words[0].strip(':'))] = int(words[1])

severity = 0
for w, d in walls.items():
    if w % (2*d-2) == 0:
        severity += w*d

print(severity)
