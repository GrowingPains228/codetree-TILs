n = int(input())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

A_arr.sort()
B_arr.sort()

isSame = True
for i in range(n) :
    if A_arr[i] != B_arr[i] :
        isSame = False
        break

print("Yes" if isSame else "No")