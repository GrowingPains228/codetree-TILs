import sys
INT_MAX = sys.maxsize
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

x_elem.sort()
y_elem.sort()
# 최소값은, x의 가운데 쯤과, y 의 가운데 쯤일 것이다.
# 따라서, 정렬을 한다음 가운데에 있는 값들 사이를 조사하면 될것이다.
ans = 0
diff_dots = INT_MAX
for i in range(len(x_elem)) :
    x_axis = x_elem[i] + 1
    for j in range(len(y_elem)) :
        y_axis = y_elem[j] + 1

        count = [0] * 4

        for x,y in dots :
            if x > x_axis :
                if y > y_axis :
                    count[0] += 1
                else :
                    count[1] += 1
            else :
                if y > y_axis :
                    count[2] += 1
                else :
                    count[3] += 1

        if diff_dots > (max(count) - min(count)) :
            diff_dots = (max(count) - min(count))
            ans = max(count)

print(ans)