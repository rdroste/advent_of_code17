
import operator

ops = {">": operator.gt, ">=": operator.ge, "==": operator.eq,
       "<": operator.lt, "<=": operator.le, "!=": operator.ne}

register = {}
with open('008_input.txt') as f:
    for line in f:
        words = line.split()

        for i in [0,4]:
            if words[i] not in register:
                register[words[i]] = 0

        if ops[words[5]](register[words[4]], int(words[6])):
            if words[1] == 'inc':
                register[words[0]] += int(words[2])
            if words[1] == 'dec':
                register[words[0]] -= int(words[2])

print(register[max(register, key=register.get)])
# print(register)
