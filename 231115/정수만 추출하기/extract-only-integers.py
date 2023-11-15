A,B = tuple(input().split())

leng_A = len(A)
leng_B = len(B)

temp_A = ""
temp_B = ""

for i in range(leng_A) :
    if not A[i].isdigit() :
        break;

    temp_A += A[i]

for i in range(leng_B) :
    if not B[i].isdigit() :
        break;

    temp_B += B[i]

print(int(temp_A) + int(temp_B))