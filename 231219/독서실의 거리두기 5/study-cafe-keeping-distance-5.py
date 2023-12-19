n = int(input())
seats = list(input())

def min_dist() :
    dist = n

    for i in range(n) :
        for j in range(i + 1, n) :
            if seats[i] == '1' and seats[j] == '1' :
                dist = min(dist, j - i)
    
    return dist

ans = 0

for i in range(n) :
    if seats[i] == '0' :
        seats[i] = '1'

        ans = max(ans, min_dist())

        seats[i] = '0'

print(ans)