class dot :
    def __init__(self, x, y, idx) :
        self.x, self.y, self.idx = x,y,idx

n = int(input())
dot_group = []
for i in range(1,n+1) :
    x,y = tuple(map(int, input().split()))
    dot_group.append(dot(x,y,i))

dot_group.sort(key=lambda d : ((abs(d.x) + abs(d.y)), d.idx))
for dot in dot_group :
    print(dot.idx)