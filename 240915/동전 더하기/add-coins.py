n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0
tempk = k
for i in range(n-1, -1, -1):
    cur_cnt = tempk//coins[i]
    tempk -= cur_cnt * coins[i]
    cnt += cur_cnt

print(cnt)