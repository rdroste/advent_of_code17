

programs = []
holding = []
with open('007_input.txt') as infile:
    for line in infile:
        words = line.split()
        programs.append(words[0])
        if len(words) > 2:
            for child in words[3:-1]:
                holding.append(child[:-1])
            holding.append(words[-1])

print([p for p in programs if p not in holding])
