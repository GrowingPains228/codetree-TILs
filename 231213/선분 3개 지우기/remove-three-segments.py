n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

cnt = 0
for  i in  range(n) :
    for j in range(i+1, n) :
        for k in range(j + 1, n) :
            line = [0] * 101
            is_meet = False
            for z in range(n) :
                if z in [i, j, k] :
                    continue

                a,b = arr[z]
                for l in range(a,b+1) :
                    line[l] += 1

                    if line[l] > 1 :
                        is_meet = True
                        break
                
            if not is_meet :
                cnt += 1


print(cnt)