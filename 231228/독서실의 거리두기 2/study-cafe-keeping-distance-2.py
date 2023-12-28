n = int(input())
seats = list(input())

sp, ep = 0,0
dis = 0
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

# 자리에 앉히고 거리를 측정한다.
if ep == -1:
    seats[ep] = '1'
else :
    seats[sp + dis//2] = '1'

ans = n
# 가장 멀리 떨어져 있는 구간을 찾는다.
for i in range(n) :
    if seats[i] == '1' :
        for j in range(i+1, n) :
            if seats[j] == '1':
                ans = min(ans, j - i)
                break

print(ans)