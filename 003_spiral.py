import math

n = 368078

l = math.ceil((math.sqrt(n)-1)/2)
ns = 2*l
rn = n - (2*l-1)**2

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

distance = abs(col) + abs(row)
print(distance)
