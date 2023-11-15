n,A = tuple(input().split())

cnt = 0
for _ in range(int(n)) :
    string = input()
    if A == string :
        cnt += 1

print(cnt)