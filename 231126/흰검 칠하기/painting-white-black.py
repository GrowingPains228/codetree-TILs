OFFSET = 100000
Max_range = 200000

class Color_Block :
    def __init__ (self, white = 0, black = 0, color = '') :
        self.white = white
        self.black = black
        self.color = color


n = int(input())
crrunt_pos = 0

checked = [ Color_Block() for _ in range(Max_range + 1)]
segment = []

for _ in range(n) :
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'L' :
        start_pos = crrunt_pos - distance + 1
        end_pos = crrunt_pos + 1
        crrunt_pos = crrunt_pos - distance + 1
    else :
        start_pos = crrunt_pos
        end_pos = crrunt_pos + distance
        crrunt_pos = crrunt_pos + distance - 1

    # direction으로 white 인지 black 인지 판별할것이다.
    segment.append((start_pos, end_pos, direction))


for (start_pos, end_pos, direction) in segment :
    for i in range(start_pos + OFFSET, end_pos + OFFSET) :
        if checked[i].white >= 2 and checked[i].black >= 2 :
            continue

        if direction == 'L' :
            checked[i].white += 1
            checked[i].color = 'w'
        else :
            checked[i].black += 1
            checked[i].color = 'b'

        if checked[i].white >= 2 and checked[i].black >= 2 :
            checked[i].color = 'g'

cnt_white = 0
cnt_black = 0
cnt_gray = 0

for elem in checked :
    if elem.color == 'w' :
        cnt_white += 1
    elif elem.color == 'b' :
        cnt_black += 1
    elif elem.color == 'g' :
        cnt_gray += 1

print(cnt_white, cnt_black, cnt_gray)