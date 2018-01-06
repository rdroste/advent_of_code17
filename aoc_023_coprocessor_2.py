
# import operator

# ops = {"sub": operator.sub, "mul": operator.mul}


# def checkifreg(w):
#     return len(w) == 1 and ord(w) > 57


# def getval(w, reg):
#     return reg[getkey(w)] if checkifreg(w) else int(w)


# def getkey(w):
#     return ord(w) - 97


# reg = [1] + 7*[0]
# with open('023_input.txt','r') as f:
#     lines = [l.strip().split(' ') for l in f]

# i = 0
# counter = 0
# while True:
#     words = lines[i]
#     key = getkey(words[1])
#     if key in [1,2]:
#         continue

#     if words[0] in ops:
#         reg[key] = ops[words[0]](reg[key], getval(words[2],reg))

#     elif words[0] == "set":
#         reg[key] = getval(words[2],reg)

#     if words[0] == "jnz" and getval(words[1],reg) != 0:
#         i += getval(words[2],reg)
#     else:
#         i += 1

#     if i < 0 or i >= len(lines):
#         print('Terminating')
#         break

#     counter += 1
#     if counter % 1001 == 0:
#         print(reg)
#         print(i)

# print(reg['h'])

x = 84 * 100 - 100000

h = 0
b = 84 * 100 - 100000
c = b - 17000
for b in range(x, x - 17000 - 1, -17):
    f = 1
    for d in range(2,b-1,-1):
        for e in range(2,b-1,-1):
            if d * e == b:
                f = 0
    if f == 0:
        h -= 1
        print(h)

print(h)
