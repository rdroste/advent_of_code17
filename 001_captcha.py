
infile = open('input.txt','r')
lines = infile.readlines()
c = int(lines[0])
# print(c)

s = str(c)
# s = '112231'

sum = 0
# for i in range(length(s)):
for i, d in enumerate(s, -1):
    if d is s[i]:
        sum = sum + int(s[i])

print(sum)
