# 원소의 수 n
n = int(input())

# n개의 리스트
arr = list(map(int, input().split()))

# count 배열을 0으로 초기화
# 편의상 배열의 index가 실제 숫자를 나타내도록 하기 위해
# 범위 + 1개의 공간을 갖는 배열로 선언(0 때문에)
count = [0 for _ in range(1000+1)]


# 1. count 배열의 등장 빈도를 센다
for elem in arr : 
    count[elem] += 1

# 2. 큰 수 부터 체크하는데, 빈도수 1 인 놈만 체크해서 최대값으로 넣어준다.
max_num = -1
for max_candidate in range(1000, -1, -1) :
    if count[max_candidate] == 1 :
        max_num = max_candidate
        break                                                                                                                                                                                              

print(max_num)