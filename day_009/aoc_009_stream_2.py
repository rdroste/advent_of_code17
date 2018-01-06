

with open('009_input.txt','r') as f:

    garbage = False
    group_level = 0
    score = 0
    garbage_count = 0
    while True:
        c = f.read(1)
        if not c:
            break

        if c == '!':
            c = f.read(1)
        elif garbage:
            if c == '>':
                garbage = False
            else:
                garbage_count += 1
        elif c == '<':
            garbage = True

print(garbage_count)
