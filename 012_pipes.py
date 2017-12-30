
progs = {}
with open('012_input.txt','r') as f:
    for line in f:
        words = line.split()
        progs[int(words[0])] = [int(p.strip(',')) for p in words[2:]]


def search(id, found):
    for p in progs[id]:
        if p not in found:
            found.append(p)
            found = search(p, found)

    return found


found = search(0, [0])
print(len(found))
