A = input()
B = input()

cnt = 0
while True :
    if A == B :
        break
    
    A = A[-1] + A[:-1]
    cnt += 1

    if cnt > len(A) :
        cnt = -1
        break

print(cnt)