MAX_NUM = 100000
n = int(input())
arr = [0] + list(map(int, input().split()))

count_array = [0] * (MAX_NUM+1)

ans = 0
j = 0
for i in range(1, n+1):
    while j + 1 <= n and count_array[arr[j+1]] == 0:
        count_array[arr[j+1]] += 1
        j += 1
    
    ans = max(ans, j - i + 1)
    count_array[arr[i]] -= 1

print(ans)