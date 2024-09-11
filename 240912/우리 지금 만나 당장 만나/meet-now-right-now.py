import math
n = int(input())
people = list(map(int, input().split()))
verse = list(map(int, input().split()))


def is_Possible(time):
    max_x1 = people[0] - verse[0] * time
    min_x2 = people[0] + verse[0] * time
    for i in range(1, n):
        x1 = people[i] - verse[i] * time
        x2 = people[i] + verse[i] * time

        max_x1 = max(max_x1, x1)
        min_x2 = min(min_x2, x2)

    return max_x1 <= min_x2


left, right = 0, 1e9
ans = 1e9

for _ in range(1000):
    mid = (left + right) / 2
    if is_Possible(mid):
        right = mid
        ans = min(ans, mid)
    else:
        left = mid

print(f"{ans:.4f}")