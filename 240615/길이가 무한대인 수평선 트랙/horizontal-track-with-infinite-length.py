from sortedcontainers import SortedSet

N, T = tuple(map(int, input().split()))
players = SortedSet()
for _ in range(N):
    p, v = tuple(map(int, input().split()))
    players.add((-p,v))

newPlayers = SortedSet()
positionDict = dict()

for _ in range(T):
    length = len(players)
    newPlayers.clear()
    positionDict.clear()
    for i in range(length):
        curr_p, velocity = players[i]
        findidx = newPlayers.bisect_right((-curr_p, _))

        if findidx != len(newPlayers):
            position, new_velocity = newPlayers[findidx]
            if velocity >= new_velocity and position <= -curr_p + velocity:
                curr_p = position
            else:
                curr_p = -curr_p + velocity
        else:
            curr_p = -curr_p + velocity

        if curr_p in positionDict:
            positionDict[curr_p] = min(positionDict[curr_p], velocity)
        else:
            positionDict[curr_p] = velocity

        newPlayers.add((curr_p, velocity))
    players.clear()

    for position, v in positionDict.items():
        startidx = newPlayers.bisect_left((position, v))
        (cur_pos, velocity) = newPlayers[startidx]
        players.add((-cur_pos, velocity))

    if len(players) == 1:
        break

print(len(players))