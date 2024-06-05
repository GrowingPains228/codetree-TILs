n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

# 시간 복잡도 n**2 이하로 끝내기.
count = dict()
for elem in arr:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

ans = 0
for i in range(n):
    count[arr[i]] -= 1
    for j in range(i):
        diff = k - arr[i] - arr[j]

        if diff in count:
            ans += count[diff]

print(ans)