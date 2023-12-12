n = int(input())

segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_area = 0
for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j + 1, n) :
            x1,y1 = segments[i]
            x2,y2 = segments[j]
            x3,y3 = segments[k]

            # y 값이 같으면 x 축에 평행함
            if y1 != y2 and y1 != y3 and y2 != y3 :
                continue
                
            # x 값이 같으면 y 축에 평행함
            if x1 != x2 and x1 != x3 and x2 != x3 :
                continue
            
            # 직각삼각형 이므로, 밑변 * 높이 = 넓이 가 됨
            area = (max(x1,x2,x3) - min(x1,x2,x3)) * (max(y1,y2,y3) - min(y1, y2, y3))
            max_area = max(max_area, area)
print(max_area)