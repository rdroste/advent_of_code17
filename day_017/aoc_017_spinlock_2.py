
step = 343

cbuffer = [0]
pos = 0
for i in range(1,50000001):
    pos = (pos + 1 + step) % i
    if pos == 0:
        cbuffer.insert(pos + 1, i)

print(cbuffer[1])
