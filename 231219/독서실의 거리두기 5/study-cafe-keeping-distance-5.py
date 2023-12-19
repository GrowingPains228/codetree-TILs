n = int(input())
seats = list(map(int, list(input())))

ans = 0
for i in range(n) :
    if seats[i] == 0 :
        distance = n + 1
        for j in range(n) :
            if i == j :
                continue

            if seats[j] == 1:
                distance = min(distance, abs(i-j))

        ans = max(ans, distance)

print(ans)