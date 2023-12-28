n = int(input())
arr = list(input().split())
for i in range(n) :
    arr[i] = ord(arr[i]) - ord('A')
order = [
    i for i in range(n)
]

ans = 0
for i in range(n) :
    for j in range(n-i-1) :
        if arr[j] < arr[j+1] :
            continue

        arr[j], arr[j+1] = arr[j+1], arr[j]
        ans += 1

print(ans)