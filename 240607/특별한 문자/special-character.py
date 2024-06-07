from collections import defaultdict
inp = input()

dic = defaultdict(int)
ans_char = ''

for i in range(len(inp)):
    dic[inp[i]] += 1

for key, value in dic.items():
    if value == 1 and ans_char == '':
        ans_char = key

print(ans_char if ans_char != '' else "None")