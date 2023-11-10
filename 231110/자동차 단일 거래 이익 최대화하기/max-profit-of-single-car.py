n = int(input())
arr = list(map(int, input().split()))

# 자동차를 사야하는 시기 : 제일 싼 시기
# 자동차를 팔아야하는 시기 : 제일 비싼 시기
# 위 두 시기에 자동차 값을 빼면 최대 이익을 낼 수 있음.
# (단, 자동차를 산 시기가 자동차를 판 시기보다 앞서야한다.)
max_idx = 0
min_idx = 0
greatest_profit = 0

for i in range(0, n) :
    for j in range(i,n) :
        if arr[i] >= arr[j] :
            continue
        
        if arr[j] - arr[i] > greatest_profit :
            greatest_profit = arr[j] - arr[i]

print(greatest_profit)