

val = [512, 191]
factor = [16807, 48271]
divisor = 2147483647

matches = 0
for i in range(int(40e6)):
    val = [(v * f) % divisor for v,f in zip(val, factor)]
    lower_bits = [v & 0xffff for v in val]
    if lower_bits[0] == lower_bits[1]:
        matches += 1

print(matches)
