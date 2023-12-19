n = int(input())
seats = list(map(int, list(input())))

idx = 0
for i in range(n) :
    if seats[i] == 0 :
        seats[i] = 1
        re_distance = 0
        for j in range(n) :
            distance = n + 1
            for k in range(n) :
                if j == k :
                    continue

                if seats[j] == 1 and seats[k] == 1 :
                    distance = min(distance, abs(j-k))
            
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