a,b = tuple(map(int, input().split()))
n = list(map(int,list(input())))

ori_val = 0
for elem in n :
    ori_val = ori_val * a + elem

n = []
while True :
    if ori_val < b :
        n.append(ori_val)
        break
    
    n.append(ori_val % b)
    ori_val //= b

for digit in n[::-1] :
    print(digit, end="")