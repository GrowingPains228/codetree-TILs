n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def is_collect(num) :
    idx = 0
    while idx < n :
        a,b = arr[idx]
        if a <= num * 2 and num * 2 <= b :
            num = num * 2
            idx += 1
        else :
            return False
    
    return True
        
ans = 10001
a,b = arr[0]
for j in range(a//2,b+1//2) :
    if is_collect(j) :
        ans = min(ans, j)

print(ans)