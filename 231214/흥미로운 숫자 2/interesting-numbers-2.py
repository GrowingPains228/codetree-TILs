x,y = tuple(map(int, input().split()))

def is_Interesting(num) :
    count = [0] * 10

    while num > 0 :
        count[num%10] += 1
        num //= 10

    cnt_1 = 0
    cnt_2 = 0
    for i in range(10) :
        if count[i] >= 2:
            cnt_2 += 1
            
        if count[i] >= 1:
            cnt_1 += 1
    
    return (cnt_1 == 2 and cnt_2 == 1)

cnt = 0
for i in range(x, y+1) : 
    if is_Interesting(i) :
        cnt += 1

print(cnt)