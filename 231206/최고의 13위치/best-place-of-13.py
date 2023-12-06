n = int(input())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

coin_num = 0
for i in range(n) :
    for j in range(n-2) :
        coins =  arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        coin_num = max(coin_num, coins)

print(coin_num)