n, k = tuple(map(int, input().split()))
numbers = [
    int(input()) for _ in range(n)
]
numbers.sort()

ans = 0
for i in range(n) :
    for j in range(i+1, n) :
        min_num, max_num = min(numbers[i:j+1]),max(numbers[i:j+1])

        if max_num - min_num <= k :
            ans = max(ans, (j-i+1))

print(ans)