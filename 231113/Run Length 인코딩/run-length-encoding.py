A = input()
new_a = []
cnt = 1
for i in range(1, len(A)) :
    if A[i-1] == A[i] :
        cnt += 1
    else :
        new_a.append(A[i-1])
        new_a.append(cnt)
        cnt = 1
    
    if i == len(A) - 1 :
        new_a.append(A[i-1])
        new_a.append(cnt)
        cnt = 1

print(len(new_a))
for elem in new_a :
    print(elem, end="")