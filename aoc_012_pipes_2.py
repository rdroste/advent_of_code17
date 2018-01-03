
progs = {}
with open('012_input.txt','r') as f:
    for line in f:
        words = line.split()
        progs[int(words[0])] = [int(p.strip(',')) for p in words[2:]]


def search(pid, found):
    for p in progs[pid]:
        if p not in found:
            found.append(p)
            found = search(p, found)

    return found


group_count = 0
while progs:
    pid = next(iter(progs))
    found = search(pid, [pid])
    group_count += 1
    for p in found:
        del progs[p]

print(group_count)
