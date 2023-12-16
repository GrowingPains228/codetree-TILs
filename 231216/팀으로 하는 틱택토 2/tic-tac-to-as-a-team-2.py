def in_range(x,y) :
    return 0 <= x and x < 3 and 0 <= y and y < 3

TickTackTo = [
    list(map(int, list(input())))
    for _ in range(3)
]

team = []
ans = 0
# 가로
for i in range(3) :
    segment = []
    for elem in TickTackTo[i][::] :
        if elem not in segment :
            segment.append(elem)

    if len(segment) == 2 and segment not in team:
        ans += 1
        team.append(segment)

# 세로
for i in range(3) :
    segment = []
    for j in range(3) :
        if TickTackTo[j][i] not in segment :
            segment.append(TickTackTo[j][i])

    if len(segment) == 2  and segment not in team:
        ans += 1
        team.append(segment)

# 대각선
segment = []
for i in range(3) :
    if TickTackTo[i][i] not in segment :
        segment.append(TickTackTo[i][i])

if len(segment) == 2  and segment not in team:
    ans += 1
    team.append(segment)

segment = []
for i in range(3) :
    if TickTackTo[i][2-i] not in segment :
        segment.append(TickTackTo[i][2-i])  

if len(segment) == 2  and segment not in team:
    ans += 1
    team.append(segment)

print(ans)