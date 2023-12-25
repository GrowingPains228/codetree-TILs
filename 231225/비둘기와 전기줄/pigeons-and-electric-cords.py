n = int(input())
Pigeon = [0] * 11
is_Pigeon_Moved = [False] * 11

cnt = 0
for i in range(n) :
    num, where = tuple(map(int, input().split()))
    if not is_Pigeon_Moved[num] :
        is_Pigeon_Moved[num] = True
        Pigeon[num] = where
    else :
        if Pigeon[num] != where :
            Pigeon[num] = where
            cnt += 1
    
print(cnt)