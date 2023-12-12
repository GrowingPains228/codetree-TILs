k,n = tuple(map(int, input().split()))

# developer[사람 순서][몇번째 경기]
developer = [
    [0 for _ in range(k)]
    for _ in range(n)
]

for i in range(k) :
    race = list(map(int, input().split()))
    # (race[j]) 번째 학생의 i 번째 레이스에서의 j위
    for j in range(n) :
        developer[race[j]-1][i] = j + 1
    
cnt = 0 
for i in range(n) :
    for j in range(n) :
        if i == j :
            continue

        tf = True
        for r in range(k) :
            if developer[i][r] < developer[j][r] :
                tf = False
                break

        cnt += 1 if tf else 0

print(cnt)