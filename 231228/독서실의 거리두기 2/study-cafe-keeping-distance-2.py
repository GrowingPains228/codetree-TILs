n = int(input())
seats = list(input())

sp, ep = 0,0
start_dis, end_dis = 0,0
# 처음에 사람이 없으면, 카운트 하기
if seats[0] == '0' :
    for i in range(1, n) :
        if seats[i] == '1' :
            start_dis = i
            break

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

# 제일 끝에 사람이 없으면, 카운트 하기
if seats[-1] == '0' :
    for i in range(n-2, -1, -1) :
        if seats[i] == '1' :
            end_dis = (n-1) - i
            break

max_dis = start_dis
max_dis = max(max_dis, end_dis)
max_dis = max(max_dis, dis//2)

if max_dis == start_dis :
    seats[0] = '1'
elif max_dis == end_dis :
    seats[-1] = '1'
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