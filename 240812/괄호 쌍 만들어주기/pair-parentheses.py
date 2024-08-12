string = list(input())
length = len(string)

L = [0] * length # (( 의 개수

for i in range(1, length):
    if string[i] == '(' and string[i-1] == '(' :
        L[i] = L[i-1] + 1
    else:
        L[i] = L[i-1]

ans = 0
for i in range(length-1):
    if string[i] == ')' and string[i+1] == ')' :
        ans += L[i]

print(ans)