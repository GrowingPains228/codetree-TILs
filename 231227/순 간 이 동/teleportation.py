A, B, x, y = tuple(map(int, input().split()))
ans = 100

# 1. 순간이동 하지 않고 바로 가는 경우
ans = min(ans, abs(B - A))
# 2. 순간이동을 사용하는 경우.
ans = min(ans, abs(A-x) + abs(B-y))
ans = min(ans, abs(A-y) + abs(B-x))
print(ans)