

h = 0
b = 84 * 100 + 100000
c = b + 17000
while b <= c:
    f = 1
    for d in range(2,b//2):
        if b % d == 0:
            h += 1
            break
    b += 17

print(h)
