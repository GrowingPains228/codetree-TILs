MAX_NUM = 10000

n,k = tuple(map(int, input().split()))
arr = [
    int(input()) for _ in range(n)
]

def range_count(l,r) :
    cnt = 0
    for elem in arr :
        if elem < l or elem > r :
            continue
    
        cnt += 1

    return cnt

ans = 0
for i in range(1, MAX_NUM + 1) :
    cnt = range_count(i, i + k)
    ans = max(ans, cnt)

print(ans)