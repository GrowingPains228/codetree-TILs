n = int(input())
seats = list(input())

sp, ep = 0,0
dis = 0
# 처음 좌석에 사람이 있는 경우를 체크
first_isvalue = True
if seats[0] == '0' :
    first_isvalue = False
    seats[0] = '1'

# 가장 멀리 떨어져 있는 구간을 찾는다.
for i in range(n) :
    if seats[i] == '1' :
        for j in range(i+1, n) :
            if seats[j] == '1':
                if dis < j-i :
                    dis = j - i
                    sp = i
                break
            else : 
                # 제일 끝에 자리가 없고 그 자리가 가장 멀다면
                if  j == n-1 :
                    if dis//2 < j-i :
                        sp ,ep = i, -1

# 처음에 값이 없었는데, 제일 먼 거리로 잡혔다면 그대로 패스
if not first_isvalue and sp == 0 :
    pass
else :
    if ep == -1:
        seats[ep] = '1'
    else :
        seats[sp + dis//2] = '1'
    
    seats[0] = '1' if first_isvalue else '0'

ans = n
# 가장 멀리 떨어져 있는 구간을 찾는다.
for i in range(n) :
    if seats[i] == '1' :
        for j in range(i+1, n) :
            if seats[j] == '1':
                ans = min(ans, j - i)
                break

print(ans)