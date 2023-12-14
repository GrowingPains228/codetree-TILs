n = int(input())
arr = list(map(int, input().split()))
ans = 0

for k in range(1, max(arr)+1) :
    count = 0
    for i in range(n) :
        for j in range(i + 1, n) :
            if abs(arr[j] - k) == abs(k - arr[i]) :
                count += 1
        
        ans = max(ans, count)

print(ans)