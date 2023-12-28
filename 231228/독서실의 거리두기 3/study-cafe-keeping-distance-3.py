n = int(input())
seats = list(input())

# 최대 거리를 가진 구간 찾기
sp, ep = 0,0 #저장해 놓을 인덱스
dis = 0
for i in range(n) :
    if seats[i] == '1' :
        for j in range(i+1, n) :
            if seats[j] == '1' :
                # 최대 구간 인덱스 저장해놓기
                if dis < j - i :
                    dis = j-i
                    sp, ep = i, j

                break
    
# 최대 구간 가운데에 사람 앉히기
seats[sp + dis//2] = '1'

ans = n
#거리 측정하기
for i in range(n) :
    if seats[i] == '1' :
        for j in range(i+1, n) :
            if seats[j] == '1' :
                # 최대 구간 인덱스 저장해놓기
                ans = min(ans, j-i)
                break

print(ans)