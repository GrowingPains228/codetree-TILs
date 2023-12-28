line = list(map(int, input().split()))

ans = 0
if line[0] + 1 == line[1] and line[1]+1 == line[2] :
    ans = 0
else :
    while True :
        if line[0] + 1 == line[1] and line[1]+1 == line[2] :
            break
        
        # 사이가 가장 먼 저리 구하기
        if line[1]- line[0] < line[2] - line[1] :
            line[0] = line[1] + 1
            line[0], line[1] = line[1], line[0]
        else :
            line[2] = line[1] - 1
            line[1], line[2] = line[2], line[1]
        
        ans += 1

print(ans)