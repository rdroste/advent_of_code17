

with open('009_input.txt','r') as f:

    garbage = False
    group_level = 0
    score = 0
    while True:
        c = f.read(1)
        if not c:
            break

        if c == '!':
            c = f.read(1)
        elif garbage:
            if c == '>':
                garbage = False
        elif c == '<':
            garbage = True
        elif c == '{':
            group_level += 1
            score += group_level
        elif c == '}':
            group_level -= 1

print(score)
