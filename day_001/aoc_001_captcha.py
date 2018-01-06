
infile = open('001_input.txt','r')
lines = infile.readlines()
s = lines[0].strip()

sum = 0
for i, d in enumerate(s, -1):
    if d is s[i]:
        sum = sum + int(s[i])

print(sum)
