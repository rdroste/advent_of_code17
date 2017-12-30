
with open('010_input.txt','r') as f:
    content = f.readline()
    lengths = [int(x.strip()) for x in content.split(',')]

n = 256
nums = list(range(0,n))
pos = 0
skip = 0
for l in lengths:

    if l > n-1:
        continue

    for i in range(0, l//2):
        x = (pos + i) % n
        y = (pos + l - i - 1) % n
        nums[x], nums[y] = nums[y], nums[x]

    pos = (pos + l + skip) % n
    skip += 1

print(nums[0]*nums[1])
