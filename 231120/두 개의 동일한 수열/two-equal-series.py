n = int(input())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

A_arr.sort()
B_arr.sort()

isSame = True
for a,b in zip(A_arr, B_arr) :
    if a != b :
        isSame = False
        break

print("Yes" if isSame else "No")