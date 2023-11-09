import sys

n = int(input())
arr = list(map(int, input().split()))
duplication_arr = []

#한번 순회해서 중복되어 있는 요소들로 구성된 리스트 만들기
for i in range(0,n-1) :
    if arr[i] not in duplication_arr:
        for j in range(i+1,n) :
            if arr[i] == arr[j]:
                duplication_arr.append(i)
                break

max_num = 0
index = 0
#내가 푼 성능이 좋지않은 코드 1
# 1. 최대값 하나를 넣고
# 2. 중복을 체크할 리스트를 하나 만들어서, 순회하면서 체크해주다.
# 2. 순회하면서 가장 최댓값 max_num 변수에 넣는다.
# 3. 중간에 똑같은 수를 만나면 break
for i in range(n) :
    if arr[i] in duplication_arr :
        continue
    
    index = i
    max_num = arr[i]
    break

if max_num == 0 :
    print(-1)
    sys.exit()

for i in range(n) :
    if arr[i] in duplication_arr or i == index:
        continue

    if max_num < arr[i] :
        max_num = arr[i]

print(max_num)