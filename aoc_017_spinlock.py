
step = 343

cbuffer = [0]
pos = 0
for i in range(1,2018):
    pos = (pos + 1 + step) % i
    cbuffer.insert(pos + 1, i)

print(cbuffer[pos+2])
