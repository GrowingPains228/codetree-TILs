MAX_TIME = 250
# N : 개발자 수
# K : 감염된 후 K번의 악수 동안만 점염병을 옮김
# P : 처음 전염병에 걸려 있는 개발자의 번호
# T : t초에 x개발자가 y개발자와 악수를 나눈 정황의 수
N, K, P, T = tuple(map(int, input().split()))

# 시간에 누가 누구와 악수를 했는가에 대한 히스토리 배열
timeline = [(0,0) for _ in range(MAX_TIME + 1)]

# 개발자에 대한 배열(감염여부 판단)
developers = [0] * (N + 1)
# 처음 전염병에 걸려 있는 개발자 세팅
developers[P] = 1

# 감염 시킬 수 있는 근황 배열
is_Inpectionable = [0] * (N + 1)
is_Inpectionable[P] = K

# 타임 라인 세팅
late_Time = 0
for _ in range(T) :
    t,x,y = tuple(map(int, input().split()))
    timeline[t] = (x, y)
    late_Time = max(late_Time,t)

# 타임 라인 꺼내서 기록하기
for i in range(1, late_Time) :
    x,y = timeline[i]

    # 해당 시간대에 아무일도 일어나지 않았다면,
    if x == 0 and y == 0 :
        continue
    
    # 하지만, 누군가 악수를 한 시간이면, 이 아래로 들어오게 된다.
    # 감염자인지 판별
    if developers[x] == 0 and developers[y] == 0 :
        continue

    # 감염자라면 여기 아래로 들어오게 된다.
    # 감염시킬 수 있는지 판단 
    # 1. 둘다 감염되어 있는 경우
    if developers[x] == 1 and developers[y] == 1 :
        is_Inpectionable[x] = is_Inpectionable[x] - 1 if is_Inpectionable[x] > 0 else 0
        is_Inpectionable[y] = is_Inpectionable[y] - 1 if is_Inpectionable[y] > 0 else 0
    # 2. x만 감염되어 있는 경우
    elif developers[x] == 1 and developers[y] == 0 :
        if is_Inpectionable[x] == 0 :
            continue

        is_Inpectionable[x] -= 1
        developers[y] = 1
        is_Inpectionable[y] = K
    # 3. y만 감염되어 있는 경우        
    elif developers[x] == 0 and developers[y] == 1 :
        if is_Inpectionable[y] == 0 :
            continue

        is_Inpectionable[y] -= 1
        developers[x] = 1
        is_Inpectionable[x] = K


for i in range(1, N + 1) :
    print(developers[i], end = "")