
import operator

ops = {"add": operator.add, "mul": operator.mul, "mod": operator.mod}


def checkifreg(w):
    if len(w) == 1 and ord(w) > 57:
        return True
    else:
        return False


def getval(w, reg):
    if checkifreg(w):
        return reg[w]
    else:
        return int(w)


reg = [{'p':0}, {'p':1}]
p1sendcounter = 0
queues = [[], []]
with open('018_input.txt','r') as f:
    lines = f.readlines()

    i = [0, 0]
    waiting = [False, False]
    while True:
        for j in range(2):
            words = lines[i[j]].strip().split(' ')

            for w in words[1:]:
                if checkifreg(w) and w not in reg[j]:
                        reg[j][w] = 0

            if words[0] in ops:
                reg[j][words[1]] = ops[words[0]](reg[j][words[1]], getval(words[2],reg[j]))

            elif words[0] == "set":
                reg[j][words[1]] = getval(words[2],reg[j])

            elif words[0] == "snd":
                queues[int(not(j))].append(getval(words[1],reg[j]))
                if j == 1:
                    p1sendcounter += 1

            elif words[0] == "rcv":
                if queues[j]:
                    reg[j][words[1]] = queues[j][0]
                    del queues[j][0]
                else:
                    waiting[j] = True
                    continue

            if words[0] == "jgz" and getval(words[1],reg[j]) > 0:
                i[j] += getval(words[2],reg[j])
            else:
                i[j] += 1

        if all(waiting):
            print('Deadlock')
            break

        if min(i) < 0 or max(i) >= len(lines):
            print('Terminating')
            break


print(p1sendcounter)
