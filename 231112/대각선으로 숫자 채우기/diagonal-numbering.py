# 기본 세팅
n,m = tuple(map(int, input().split()))
num = 1
arr_2d = [
    [ 0 for _ in range(m)]
    for _ in range(n)
]

# 알고리즘
# 1. [(0,0)] , [(0,1), (1,0)] , [(0,2),(1,1), (2,0)], ...
# 2. 처음 m 만큼 이동하면서 count 한다음
# 3. n만큼 다시 이동하면서 count 한다.
# 먼저 열 개수만큼 순회한다.

cur_columns = j = 0
cur_rows = i = 0

# 열에 대해서 먼저 돌아준다.
while cur_columns < m :
    j = cur_columns # 이전에 수행했던 열 번호 다음에서 시작
    i = 0
    while i < n and j >= 0 :
        arr_2d[i][j] = num
        num += 1
        j -= 1
        i += 1
    cur_columns += 1

# 제일 끝 열에서 행에 대해서 돌아준다.
# 행 시작 부분은 index = 1 에서 부터 시작한다.
# 근데 n = 1 인 행열이 있을 수 있으므로 그에대한 조건 처리 해주기
cur_rows = 1 if n != 1 else n
while cur_rows < n :
    i = cur_rows
    j = m-1 # 
    while i < n and j >= 0 :
        arr_2d[i][j] = num
        num += 1
        j -= 1
        i += 1
    cur_rows += 1


for row in arr_2d :
    for elem in row :
        print(elem, end = " ")
    print()