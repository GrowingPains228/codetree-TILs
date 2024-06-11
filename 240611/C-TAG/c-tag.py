n,m = tuple(map(int, input().split()))
list_A = [list(input()) for _ in range(n)]
list_B = [list(input()) for _ in range(n)]

ans = 0
s = set()


def test_location(x, y, z):
    s.clear()

    for i in range(n):
        s.add(list_A[i][x] + list_A[i][y] + list_A[i][z])
    
    for i in range(n):
        if (list_B[i][x] + list_B[i][y] + list_B[i][z]) in s:
            return False
    
    return True


for i in range(m-2):
    for j in range(i+1, m-1):
        for k in range(j+1, m):
            if test_location(i, j, k):
                ans += 1

print(ans)