import math

n = 368078


def layer_end(l):
    return (2*l+1)**2


l = math.ceil((math.sqrt(n)-1)/2)
ple = layer_end(l-1)
ns = 2*l
rn = n-ple

if rn >= 3*ns:
    col = rn - 3*ns - l
    row = -l
elif rn > 2*ns:
    col = -l
    row = 2*ns - rn + l
elif rn >= ns:
    col = ns - rn + l
    row = l
else:
    col = l
    row = rn - l

print(col)
print(row)

distance = abs(col) + abs(row)
print(distance)
