
import operator

ops = {"sub": operator.sub, "mul": operator.mul}


def checkifreg(w):
    return len(w) == 1 and ord(w) > 57


def getval(w, reg):
    return reg[w] if checkifreg(w) else int(w)


reg = {}
for c in range(97,97+8):
    reg[chr(c)] = 0
mul_counter = 0
with open('023_input.txt','r') as f:
    lines = [l.strip().split(' ') for l in f]

i = 0
counter = 0
while True:
    words = lines[i]

    if words[0] == "mul":
        mul_counter += 1

    if words[0] in ops:
        reg[words[1]] = ops[words[0]](reg[words[1]], getval(words[2],reg))

    elif words[0] == "set":
        reg[words[1]] = getval(words[2],reg)

    if words[0] == "jnz" and getval(words[1],reg) != 0:
        i += getval(words[2],reg)
    else:
        i += 1

    if i < 0 or i >= len(lines):
        print('Terminating')
        break

print(mul_counter)
print(reg['h'])
