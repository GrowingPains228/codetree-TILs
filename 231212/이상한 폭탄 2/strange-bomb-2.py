n,k = tuple(map(int, input().split()))

arr = [
    int(input()) for _ in range(n)
]

def distance(i,j) :
    if i < j :
        i,j = j,i

    dis1 = i - j
    dis2 = (n-i) + j
    return min(dis1, dis2)

bomb_max = -1
for i in range(n) :
    for j in range(n) :
        if i == j or arr[i] != arr[j]:
            continue

        if distance(i,j) <= k :
            bomb_max = max(bomb_max, arr[i])

print(bomb_max)