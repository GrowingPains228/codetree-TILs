import sys
n = int(input())

dots = [ ]
x_elem = []
y_elem = []
for _ in range(n) :
    x,y = tuple(map(int ,input().split()))

    dots.append((x,y))

    if x not in x_elem :
        x_elem.append(x)
    if y not in y_elem :
        y_elem.append(y)


ans = 0
#y와 나란하게 3개 거나 x와 나란하게 3개면 직선 3개로 모두 지나게 하는것이 가능.
if len(x_elem) == 3 or len(y_elem) == 3:
    ans = 1
    print(ans)
    sys.exit()

# x축과 나란하게 1개 y축과 나란하게 2개
for i in range(len(x_elem)) :
    for j in range(i+1, len(x_elem)) :
        for k in range(len(y_elem)) :
            cnt = 0

            for (x,y) in dots :
                if x != x_elem[i] and x != x_elem[j] and y != y_elem[k] :
                    break
                cnt += 1
            
            if cnt == n:
                ans = 1
                print(ans)
                sys.exit()

# x축과 나란하게 2개 y축과 나란하게 1개
for i in range(len(x_elem)) :
    for j in range(len(y_elem)) :
        for k in range(j+1, len(y_elem)) :
            cnt = 0

            for (x,y) in dots :
                if x != x_elem[i] and y != y_elem[j] and y != y_elem[k] :
                    break
                cnt += 1
            
            if cnt == n:
                ans = 1
                print(ans)
                sys.exit()
        
print(ans)