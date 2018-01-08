
import math


def intersectioncheck(traj, p1, p2):
    intersections = None
    for dim in range(3):
        roots = []
        a = 0.5*(traj[p1][2][dim] - traj[p2][2][dim])
        b = a + (traj[p1][1][dim] - traj[p2][1][dim])
        c = traj[p1][0][dim] - traj[p2][0][dim]
        if a != 0:
            det = b**2 - 4*a*c
            if det >= 0:
                roots = [(-b + f*math.sqrt(det))/(2*a) for f in [-1,1]]
        elif b != 0:
            roots = [-c/b]
        elif c == 0:
            continue
        roots = list(set([t for t in roots if (t >= 0 and t % 1. == 0)]))
        if intersections is None:
            intersections = roots
        else:
            intersections = [t for t in roots if t in intersections]
        if not intersections:
            break
    if intersections is None:
        intersections = [0]
    return intersections


traj = []
with open('020_input.txt') as f:
    for i, line in enumerate(f):
        words = line.strip().split(' ')
        traj.append([[int(a) for a in w[3:-1].strip('>').split(',')] for w in words])

collision_candidates = {}
for p1 in range(len(traj)-1):
    for p2 in range(p1+1,len(traj)):
        intersections = intersectioncheck(traj, p1, p2)
        for t in intersections:
            if t in collision_candidates:
                collision_candidates[t] += [p1,p2]
            else:
                collision_candidates[t] = [p1,p2]

collision_times = list(collision_candidates.keys())
collision_times.sort()

alive = [1] * len(traj)
for t in collision_times:
    ps = [p for p in list(set(collision_candidates[t])) if alive[p]]
    if len(ps) > 1:
        for p in ps:
            alive[p] = 0

print(sum(alive))
