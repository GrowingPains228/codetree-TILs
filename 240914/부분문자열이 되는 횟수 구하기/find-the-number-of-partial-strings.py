A = input()
B = input()
removeList = list(map(int, input().split()))

n = len(A)
m = len(B)
skip = [False] * n


def is_possible(mid):
    b_idx  = 0
    for i in range(mid):
        skip[removeList[i] - 1] = True
    
    for i in range(n):
        if skip[i]:
            continue
        if b_idx < m and A[i] == B[b_idx]:
            b_idx += 1

    return b_idx == m


left, right = 0, n
ans = -1

while left <= right:
    mid = (left + right)//2
    if is_possible(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1
    
    for i in range(mid):
        skip[removeList[i] - 1] = False

print(ans + 1)