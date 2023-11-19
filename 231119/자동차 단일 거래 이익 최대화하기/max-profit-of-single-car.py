# 입력 및 정의 :
n = int(input())
arr = list(map(int, input().split()))

# 최대 일때만 갱신해주기.
max_benefit = 0

for i in range(n-1) :
    for j in range(i,n) :
        # 이익이 더 크다면 갱신해주기
        if arr[j]-arr[i] > max_benefit :
            max_benefit = arr[j]-arr[i]
print(max_benefit)