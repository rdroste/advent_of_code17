

from knothash import knothash2
from functools import reduce


with open('010_input.txt','r') as f:
    content = f.readline().strip()

print(knothash2(content))
