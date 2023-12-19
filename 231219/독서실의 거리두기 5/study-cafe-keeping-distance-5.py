n = int(input())
seats = list(map(int, list(input())))

idx = 0
re_distance = 0
for i in range(n) :
    if seats[i] == 0 :
        # 임의로 좌석에 앉히고 거리를 측정한다.
        seats[i] = 1
        distance = n + 1
        for j in range(n) :
            if seats[j] == 1 :
                for k in range(j+1, n) :
                    if j == k :
                        continue
                    # 가장 가까운 거리에 있는 좌석의 거리값을 측정한다.
                    if seats[k] == 1 :
                        distance = min(distance, abs(k - j))
        # 그 거리값이 가장 큰 것을 가져온다.
        if re_distance < distance :
            idx = i
            re_distance = distance

        seats[i] = 0
seats[idx] = 1
ans = n + 1
for i in range(n) :
    for j in range(n) :
        if i == j :
            continue
        
        if seats[i] == 1 and seats[j] == 1 :
            ans = min(abs(i-j), ans)

print(ans)