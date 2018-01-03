
import operator

ops = {">": operator.gt, ">=": operator.ge, "==": operator.eq,
       "<": operator.lt, "<=": operator.le, "!=": operator.ne,
       "inc": operator.__iadd__, "dec": operator.__isub__}

register = {}
max_val = 0
with open('008_input.txt') as f:
    for line in f:
        words = line.split()

        for i in [0,4]:
            if words[i] not in register:
                register[words[i]] = 0

        if ops[words[5]](register[words[4]], int(words[6])):
            register[words[0]] = ops[words[1]](register[words[0]], int(words[2]))
            max_val = max(max_val, register[max(register, key=register.get)])

print(max_val)
