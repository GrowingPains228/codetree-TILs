from sortedcontainers import SortedSet

N, T = tuple(map(int, input().split()))
players = SortedSet()
for _ in range(N):
    p, v = tuple(map(int, input().split()))
    players.add((-p,v))

newPlayers = SortedSet()
checkV = dict()
for _ in range(T):
    length = len(players)
    newPlayers.clear()
    checkV.clear()
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

        checkV[velocity] = 1
        newPlayers.add((curr_p, velocity))

    players.clear()
    
    for i in range(len(newPlayers)):
        p,v = newPlayers[i]
        players.add((-p,v))

    if len(players) == 1 or len(checkV) == 1:
        break

print(len(players))