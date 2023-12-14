x,y = tuple(map(int, input().split()))

def is_Interesting(num) :
    #set 을 이용해서 간단하게 구현하기
    s = list(str(num))
    s = set(s)
    if len(s) == 2:
        return True
    else :
        return False

cnt = 0
for i in range(x, y+1) : 
    if is_Interesting(i) :
        cnt += 1

print(cnt)