import sys
n = int(input())
numbers = list(map(int, input().split()))
temp_arr = numbers[::]
temp_arr.sort()
# 두번째로 작은 숫자가 무엇인지 일단 판별
first = temp_arr[0]
second = -1
for i in range(1, n) :
    if temp_arr[i] == first :
        continue
    
    second = temp_arr[i]
    # 두번째로 작은 숫자가 여러개라면 -1 출력
    if i + 1 < n and temp_arr[i] == temp_arr[i+1] :
        second = -1

    break
    
if second == -1 :
    print(-1)
    sys.exit()

for i in range(n) :
    if numbers[i] == second :
        second = i
        break   

print(second+1)