import sys
n = int(input())
arr = list(map(int, input().split()))

# 3개의 숫자를 골라 최대값을 구하기 위해서는 전부 음수인수만 모아놓았는데 그중에 0이 있는지, 
# 1. 모두 양수인 것만 고른다
# 2. 한개는 양수, 두개는 음수인 것을 고른다.
# 3. 모든 수가 모두 0 이하면 0 이 가장 큰 수
# 위 3 가지 경우를 비교해 보면된다.

# 3.모든 수가 모두 0 이하면 0 이 가장 큰 수이므로, 0 을 출력해주고 종료 그게 아니라면 다음 넘어가기
max_num = max(arr)
all_mius = True if max_num == 0 else False
if all_mius :
    print(0)
    sys.exit()

ans = 0
# 첫번째 케이스, 모두 양수인 경우
for i in range(n) :
    if arr[i] > 0 :
        for j in range(i + 1, n) :
            if arr[j] > 0 :
                for k in range(j + 1, n) :
                    if arr[k] > 0 :
                        ans = max(ans, arr[i] * arr[j] * arr[k])

# 두번째 케이스, 한개가 양수, 두개가 음수인 경우
for i in range(n) :
    if arr[i] > 0 :
        for j in range(n) :
            if i == j or arr[j] > 0:
                continue
            
            for k in range(n) :
                if i == k or j == k or arr[k] > 0:
                    continue

                ans = max(ans, arr[i] * arr[j] * arr[k])
    else :
        for j in range(n) :
            if i == j :
                continue
            
            if arr[j] > 0 :
                for k in range(n) :
                    if i == k or j == k or arr[k] > 0:
                        continue

                    ans = max(ans, arr[i] * arr[j] * arr[k])
            else :
                for k in range(n) :
                    if i == k or j == k or arr[k] < 0:
                        continue

                    ans = max(ans, arr[i] * arr[j] * arr[k])

print(ans)