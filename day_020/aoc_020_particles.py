

max_accel = []
with open('020_input.txt') as f:
    for i, line in enumerate(f):
        words = line.strip().split(' ')
        accels = [abs(int(a)) for a in words[2][3:-1].split(',')]
        max_accel.append(max(accels))

minima = [i for i,a in enumerate(max_accel) if a == min(max_accel)]
print(minima)

# max_velo = []
# if len(minima) > 1:
#     with open('020_input.txt') as f:
#         for i, line in enumerate(f):
#             if i in minima:
#                 words = line.strip().split(' ')
#                 print(words)
#                 velo = [abs(int(v)) for v in words[1][3:-2].split(',')]
#                 max_velo.append(max(velo))
#     print(minima[max_velo.index(min(max_velo))])
# else:
#     print(minima[0])
