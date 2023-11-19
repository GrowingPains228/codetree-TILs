n = int(input())
price = list(map(int, input().split()))

# 배열을 앞에서부터 순회하며 최솟값을 갱신함
# 각 원소에 대하여 해당 시점의 최솟값의 차이가 최대가 될 때를 갱신해줌
max_benefit = 0
min_price = price[0]

for i in range(n) :
    benefit = price[i] - min_price

    # 이익이 더 있는지 비교
    if max_benefit < benefit :
        max_benefit = benefit

    # 현재까지의 최솟값과 비교
    if price[i] < min_price :
        min_price = price[i]

print(max_benefit)