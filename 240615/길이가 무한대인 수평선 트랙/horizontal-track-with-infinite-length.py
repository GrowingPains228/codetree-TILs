from sortedcontainers import SortedSet

# 입력 받기
N, T = tuple(map(int, input().split()))
# TreeSet 정의
players = SortedSet()
for _ in range(N):
    p, v = tuple(map(int, input().split()))
    players.add((-p,v))

# 임시 TreeSet 정의
newPlayers = SortedSet()
velocity_dic = set()

# 시간이 자동으로 끝나는 조건을 확인한다.
# 총 플레이어가 1명이 된 경우, 남아있는 그룹들의 속도가 전부 똑같은 경우, (위치, 속도)가 다르지만 오름차순인 경우
# 
def IsEnd():
    length = len(players)
    if length == 1:
        return True

    if len(velocity_dic) == 1:
        return True

    for i in range(1, length):
        (p1, v1), (p2, v2) = players[i-1], players[i]
        if v2 > v1 :
            return False
    
    return True


# T분 만큼 돌면서 실행해주기.
for _ in range(T):
    length = len(players)
    newPlayers.clear()
    velocity_dic.clear()
    #시작복잡도 : NlogN
    for i in range(length):
        curr_p, velocity = players[i]
        findidx = newPlayers.bisect_right((-curr_p, _))

        if findidx != len(newPlayers):
            position, new_velocity = newPlayers[findidx]
            if velocity >= new_velocity and position <= -curr_p + velocity:
                curr_p, velocity = position, new_velocity
            else:
                curr_p = -curr_p + velocity
        else:
            curr_p = -curr_p + velocity

        newPlayers.add((curr_p, velocity))
        velocity_dic.add(velocity)

    players.clear()
    #시작복잡도 : NlogN
    for i in range(len(newPlayers)):
        p,v = newPlayers[i]
        players.add((-p,v))

    if IsEnd():
        break

print(len(players))