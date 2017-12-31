

val = [512, 191]
factor = [16807, 48271]
divisor = 2147483647

lower_bits = [[],[]]
count = [0,0]
terminate = False
while not terminate:
    val = [(v * f) % divisor for v,f in zip(val, factor)]
    for i in range(2):
        if val[i] % (4*(i+1)) == 0:
            lower_bits[i].append(val[i] & 0xffff)
            count[i] += 1
            if min(count) == 5e6:
                terminate = True

matches = 0
for i in range(int(5e6)):
    if lower_bits[0][i] == lower_bits[1][i]:
        matches += 1

print(matches)
