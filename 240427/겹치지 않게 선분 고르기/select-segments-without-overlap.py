MAX_LENGTH = 1000
Overlap = True
# 입력
n =  int(input())
ans = 0
cnt = 0
dot_arr = []
for _ in range(n):
    (x1, x2) = tuple(map(int, input().split()))
    dot_arr.append((x1, x2))
# 전체 선분의 리스트를 미리 정의
x_grid = [ False for _ in range(MAX_LENGTH + 1)]

# 두 선분을 추출해서 비교한다. => 이거 맞나..? 단순히 두 선분만 비교하면 괜찮은데,
# 이게 재귀 함수다 보니깐, 두 선분을 인자로 받아올 수 있을지 의문이다.
def Is_Overlap(x1, x2):
    return any([x_grid[i] for i in range(x1, x2+1)])


def Choose_line(idx):
    global cnt
    (x1, x2) = dot_arr[idx]
    for i in range(x1, x2+1):
        x_grid[i] = True
    cnt += 1


def UnChosse_line(idx):
    global cnt
    (x1, x2) = dot_arr[idx]
    for i in range(x1, x2+1):
        x_grid[i] = False
    cnt -= 1


def Draw_Line(idx):
    global ans
    if idx == n:
        ans = max(ans, cnt)
        return
    
    (x1, x2) = dot_arr[idx]
    if Is_Overlap(x1, x2) :
        Draw_Line(idx + 1)
    else :
        Choose_line(idx)
        Draw_Line(idx+1)
        UnChosse_line(idx)
        Draw_Line(idx+1)

Draw_Line(0)
print(ans)