n,m = tuple(map(int, input().split()))
list_A = [list(input()) for _ in range(n)]
list_B = [list(input()) for _ in range(n)]
ans = 0
for i in range(m-2):
    for j in range(i+1, m-1):
        for k in range(j+1, m):
            sa, sb = set(), set()
            for z in range(n):
                string_a = list_A[z][i] + list_A[z][j] + list_A[z][k]
                string_b = list_B[z][i] + list_B[z][j] + list_B[z][k]
                sa.add(string_a)
                sb.add(string_b)
        
            tf = True
            for elem in sb:
                if elem in sa:
                    tf = False
                    break

            if tf:
                ans += 1

print(ans)