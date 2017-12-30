
def knothash(lengths, nums, pos, skip):
    n = len(nums)
    for l in lengths:

        if l > n-1:
            continue

        for i in range(0, l//2):
            x = (pos + i) % n
            y = (pos + l - i - 1) % n
            nums[x], nums[y] = nums[y], nums[x]

        pos = (pos + l + skip) % n
        skip += 1

    return nums, pos, skip


with open('010_input.txt','r') as f:
    content = f.readline()
    lengths = [int(x) for x in content.strip().split(',')]

nums = knothash(lengths, list(range(0,256)), 0, 0)[0]

print(nums[0]*nums[1])
