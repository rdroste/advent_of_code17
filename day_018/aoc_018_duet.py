
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


reg = {}
sound = None
with open('018_input.txt','r') as f:
    lines = f.readlines()

    i = 0
    while True:
        words = lines[i].strip().split(' ')

        for w in words[1:]:
            if checkifreg(w) and w not in reg:
                    reg[w] = 0

        if words[0] in ops:
            reg[words[1]] = ops[words[0]](reg[words[1]], getval(words[2],reg))

        elif words[0] == "set":
            reg[words[1]] = getval(words[2],reg)

        elif words[0] == "snd":
            sound = getval(words[1],reg)

        elif words[0] == "rcv" and getval(words[1],reg) != 0:
                break

        if words[0] == "jgz" and getval(words[1],reg) > 0:
            i += getval(words[2],reg)
        else:
            i += 1

        if i < 0 or i >= len(lines):
            print('Terminating')
            break


print(sound)
