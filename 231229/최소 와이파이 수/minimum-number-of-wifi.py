n,m = tuple(map(int, input().split()))
seat = list(map(int, input().split()))

cnt = 0
idx = 0
while idx < n :
    if seat[idx] == 0 :
        idx += 1
        continue
    
    # 손님이 앉아 있는데, 와이파이 존이 아니라면, 
    cnt += 1 #와이파이 설치하고 
    idx += m * 2 + 1 # 영향권 밖으로 보내버리기

print(cnt)