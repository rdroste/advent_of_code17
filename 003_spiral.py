import math

n = 368078
# n=28
# n=25

# for i in range(2,n):


layer_end = lambda l: (2*l+1)**2
# layer_n = layer_end - (2*l-2)^2

l = math.ceil((math.sqrt(n)-1)/2)
ple = layer_end(l-1)
# le = layer_end(l)
# nl = le - ple
ns = 2*l
rn = n-ple

print(l)
print(ple)
# print(le)
# print(nl)
print(4*ns)

# row =
# col =

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
