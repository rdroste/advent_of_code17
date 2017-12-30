
infile = open('001_input.txt','r')
lines = infile.readlines()
s = lines[0].strip()

sum = 0
l = len(s)
for i, d in enumerate(s):
    if d is s[(i+l//2) % l]:
        sum = sum + int(s[i])

print(sum)
