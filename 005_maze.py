

maze = []
with open('005_input.txt','r') as infile:
    content = infile.readlines()
maze = [int(s) for s in content]

pos = 0
size = len(maze)
caught = True
steps = 0
while caught:

    steps = steps + 1
    jump = maze[pos]
    maze[pos] = maze[pos] + 1
    pos = pos + jump

    if pos < 0 or pos >= size:
        caught = False

print(steps)
