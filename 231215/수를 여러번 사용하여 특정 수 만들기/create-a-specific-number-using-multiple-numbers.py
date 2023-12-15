a,b,c = tuple(map(int, input().split()))

n1 = c // a
n2 = c // b

ans = 0
for i in range(n1 + 1) :
    cnt_A = i
    for j in range(n2 + 1) :
        cnt_B = j

        sum_num = cnt_A * a + cnt_B * b
        if c >= sum_num :
            ans = max(sum_num, ans)

print(ans)