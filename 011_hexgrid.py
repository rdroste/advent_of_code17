
movements = {'n':[0,1], 'ne':[1,0.5], 'e':[1,0], 'se':[1,-0.5], 's':[0,-1], 'sw':[-1,-0.5], 'w':[-1,0], 'nw':[-1,0.5]}

with open('011_input.txt','r') as f:
    contents = f.readline()
    path = contents.strip().split(',')

pos = [0,0]

for move in path:
    pos = [sum(p) for p in zip(pos, movements[move])]

# distance = max(pos) + abs(pos[1]-pos[0])
pos = [abs(p) for p in pos]
distance = pos[0] + max(0, pos[1] - pos[0]/2)
print(distance)
