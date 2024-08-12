string = list(input())
length = len(string)

R = [0] * length # )) 의 개수
L = [0] * length # (( 의 개수

for i in range(length-2, -1, -1):
    if string[i] == ')' and string[i+1] == ')' :
        R[i] = R[i+1] + 1
    else:
        R[i] = R[i+1]


for i in range(1, length):
    if string[i] == '(' and string[i-1] == '(' :
        L[i] = L[i-1] + 1
    else:
        L[i] = L[i-1]

ans = 0
for i in range(length-1):
    ans = max(ans, L[i] * R[i+1])

print(ans)