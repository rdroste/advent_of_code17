

with open('019_input.txt','r') as f:
    nw = []
    for line in f:
        nw.append(list(line.strip('\n')))


def getchr(pos):
    return nw[pos[0]][pos[1]]


def move(pos, direction):
    if direction == 'n':
        pos[0] -= 1
    elif direction == 'w':
        pos[1] += 1
    elif direction == 's':
        pos[0] += 1
    elif direction == 'e':
        pos[1] -= 1
    return pos


letters = ''
pos = [0,13]
direction = 's'
while True:
    c = getchr(pos)
    if c == '+':
        newpos = pos.copy()
        if direction in ['n', 's']:
            if getchr(move(newpos, 'w')) is not ' ':
                direction = 'w'
            else:
                direction = 'e'
        else:
            if getchr(move(newpos, 'n')) is not ' ':
                direction = 'n'
            else:
                direction = 's'
    elif c == ' ':
        break
    elif c not in ['|', '-']:
        letters += c

    pos = move(pos, direction)

print(letters)
