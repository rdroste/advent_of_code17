
infile = open('input.txt','r')
lines = infile.readlines()
c = int(lines[0])
s = str(c)

sum = 0
for i, d in enumerate(s, -1):
    if d is s[i]:
        sum = sum + int(s[i])

print(sum)
