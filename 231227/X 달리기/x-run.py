# 거리 입력 받기
x = int(input())

# 현재 속도
cur_v = 1
# 현재 거리
dis = 0
#현재 소요 시간
time = 0

# 최고 속도 까지 올리기
while dis < x//2 :
    next_d = cur_v * 1
    if dis + next_d >= x//2 :
        break
    time += 1
    dis += next_d
    cur_v += 1

if x//2 == dis :
    time *= 2
elif x - dis*2 > cur_v :
    time = 2*time + 2
else :
    time = 2*time + 1

print(time)