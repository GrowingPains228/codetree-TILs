n = int(input())
seat = list(input())

ans = 0
for i in range(n) :
    if seat[i] == '0' :
        seat[i] = '1'
        for j in range(i+1, n) :
            if seat[j] == '0' :
                seat[j] = '1'
                
                # 여기서 거리 측정
                cur_idx = 0
                for z in range(n) :
                    if seat[z] == '1' :
                        cur_idx = z
                        break

                distance = n
                for k in range(1, n) :
                    if seat[k] == '1' :
                        distance = min(distance, k - cur_idx)
                        cur_idx = k
                ans = max(ans, distance)

                seat[j] = '0'
        
        seat[i] = '0'

print(ans)