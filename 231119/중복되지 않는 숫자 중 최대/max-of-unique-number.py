# 시간 복잡도가 O(N*M)인 방법
Max_Range = 1000

# 빈도를 나타낼 배열
arr = [0 for _ in range(Max_Range + 1)]

n = int(input())
input_arr = list(map(int, input().split()))

# 입력된 배열에서 하나씩 꺼내서 빈도 배열에 등장 빈도를 증감시킨다.
for elem in input_arr :
    arr[elem] += 1

# 배열에서 등장 빈도가 1 인 것들만 탐색해서 그중에 제일 큰 수만 등장 시킨다.
# 뒤에서 부터 탐색하면 더 빠르게 찾을 수 있을 것이다.
max_num = -1
for i in range(Max_Range , -1 , -1) :
    if arr[i] == 1 :
        max_num = i
        break

print(max_num)