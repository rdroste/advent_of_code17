
from knothash import knothash

with open('010_input.txt','r') as f:
    content = f.readline()
    lengths = [int(x) for x in content.strip().split(',')]

nums = knothash(lengths, list(range(0,256)), 0, 0)[0]

print(nums[0]*nums[1])