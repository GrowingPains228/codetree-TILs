A = input()
B = input()

cnt = 0
leng_A = len(A)
leng_B = len(B)

for i in range(leng_A - leng_B + 1) :
    if B == A[i:i+leng_B] :
        cnt += 1

print(cnt)