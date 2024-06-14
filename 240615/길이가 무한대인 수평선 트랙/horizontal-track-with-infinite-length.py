from sortedcontainers import SortedSet

N, T = tuple(map(int, input().split()))
players = SortedSet()
for _ in range(N):
    p, v = tuple(map(int, input().split()))
    players.add((p,v))

newPlayers = SortedSet()
positionDict = dict()

for _ in range(T):
    length = len(players)
    newPlayers.clear()
    positionDict.clear()
    for i in range(length):
        curr_p, velocity = players[i]
        curr_p = curr_p + velocity
        if curr_p in positionDict:
            positionDict[curr_p] += 1
        else:
            positionDict[curr_p] = 1
        newPlayers.add((curr_p, velocity))
    
    players.clear()

    for position, _ in positionDict.items():
        startidx = newPlayers.bisect_left((position, _))
        players.add(newPlayers[startidx])
    

print(len(players))