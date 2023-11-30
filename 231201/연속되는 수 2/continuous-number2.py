N = int(input())

continue_cnt = 0
max_cnt = 0
curNum = 0
for i in range(N) :
    num = int(input())

    # 제일 처음 실행해줄때는, 이걸로 한번 지나가준다.
    if i == 0 :
        curNum = num
        continue_cnt = 1
        max_cnt = 1
        continue

    if curNum == num :
        continue_cnt += 1
    else :
        curNum = num
        continue_cnt = 1
        
    max_cnt = max(max_cnt, continue_cnt)

print(max_cnt)