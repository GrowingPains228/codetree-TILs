from collections import defaultdict
import sys

inp = input()
dic = defaultdict(int)

for i in range(len(inp)):
    dic[inp[i]] += 1

for elem in inp:
    if dic[elem] == 1:
        print(elem)
        sys.exit()

print("None")