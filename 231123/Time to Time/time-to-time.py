a,b,c,d = tuple(map(int, input().split()))

elapsed_time = 0
# 처음 해설에서 말하고 있는 방식 = 맘에안듬.
while True : 
    if a == c and b == d :
        break
    
    elapsed_time += 1
    b += 1

    if b == 60 :
        a += 1
        b = 0
    
print(elapsed_time)