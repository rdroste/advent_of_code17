
from aoc_007_towers import getbottom


programs = {}
weights = {}
with open('007_input.txt') as infile:
    for line in infile:
        words = [w.strip('(),') for w in line.split()]
        prog = words[0]
        weights[prog] = int(words[1])
        programs[prog] = words[3:]


def checkweights(prog):

    towerweights, invalid_program = [], []
    for i, p in enumerate(programs[prog]):
        this_towerweights, invalid_program = checkweights(p)
        towerweights.append(this_towerweights)
        if invalid_program:
            if len(invalid_program) == 1:
                return 0, invalid_program
            elif i == 0:
                towerweights[1] = checkweights(programs[prog][1])[0]
            elif len(invalid_program) > 2:
                print("ERROR: len(invalid_program) > 2")
                print(invalid_program)
            break

    if not invalid_program:
        if len(set(towerweights)) <= 1:
            return sum(towerweights + [weights[prog]]), []
        elif len(towerweights) > 2:
            invalid_program_index = towerweights.index(min(set(towerweights), key=towerweights.count))
            valid_program_index = int(not(invalid_program_index))
            invalid_program = programs[prog][invalid_program_index]
            corrected_program_weight = weights[invalid_program] + towerweights[valid_program_index] - towerweights[invalid_program_index]
            print(corrected_program_weight)
            return 0, [invalid_program]
        else:
            return 0, [programs[prog]]

    else:
        if len(invalid_program) != 2:
            print("ERROR: len(invalid_program) > 2")
        sums = [weights[p] + 2*weights[t] for t in invalid_program]
        correct_sum = towerweights[int(not(i))]
        invalid_program = [t for j,t in enumerate(invalid_program) if sums[j] != correct_sum]
        corrected_program_weight = weights[invalid_program] + correct_sum - towerweights[i]
        print(corrected_program_weight)


bottom = getbottom()
print(checkweights(bottom)[1])
