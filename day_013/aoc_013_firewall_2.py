
walls = {}
with open('013_input.txt','r') as f:
    for line in f:
        words = line.split()
        walls[int(words[0].strip(':'))] = int(words[1])


delay = 0
while True:
    caught = False
    for w, d in walls.items():
        if (w+delay) % (2*d-2) == 0:
            caught = True
            break
    if not caught:
        break
    else:
        delay += 1


print(delay)
