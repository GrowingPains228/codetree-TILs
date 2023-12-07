n = int(input())
arr = [
    list(map(int, input().split())) for _ in range(n)
]

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < n

max_coin = -1
for i in range(n) :
    for j in range(n-2) :
        first_coins = sum(arr[i][j : j+3])
        for k in range(n) :
            if k == i :
                for z in range(j+3, n-2) :
                    if not in_range(k,z+2) :
                        continue
                    
                    second_coins = sum(arr[k][z : z+3])
                    max_coin = max(max_coin, (first_coins + second_coins))
            else :
                for z in range(n-2) :
                    if not in_range(k,z+2) :
                        continue
                    
                    second_coins = sum(arr[k][z : z+3])
                    max_coin = max(max_coin, (first_coins + second_coins))

print(max_coin)