

max_accel = 0
part = 0
with open('020_input.txt') as f:
    for i, line in enumerate(f):
        words = line.strip().split(' ')
        accels = [abs(int(a)) for a in words[2][3:-1].split(',')]
        this_max_accel = sum(accels)
        # print(this_max_accel)
        if this_max_accel > max_accel:
            part = i
            max_accel = this_max_accel

print(part)
