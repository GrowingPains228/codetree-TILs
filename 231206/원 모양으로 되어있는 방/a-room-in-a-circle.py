import sys

INT_MAX = sys.maxsize
n = int(input())

room = [
    int(input()) for _ in range(n)
]

ans = INT_MAX

for i in range(n) :
    temp_ans = 0
    for j in range(n) :
        distance = (j - i) if i <= j else (n - i + j)

        temp_ans += (room[j] * distance)

    ans = min(ans, temp_ans)

print(ans)