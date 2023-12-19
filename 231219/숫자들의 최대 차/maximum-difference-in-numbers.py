n, k = tuple(map(int, input().split()))
numbers = [
    int(input()) for _ in range(n)
]
numbers.sort()

ans = 0
for i in range(n) :
    for j in range(i+1, n) :
        min_num, max_num = min(numbers[i:j]),max(numbers[i:j])

        if max_num - min_num <= 3 :
            ans = max(ans, (j-i))

print(ans)