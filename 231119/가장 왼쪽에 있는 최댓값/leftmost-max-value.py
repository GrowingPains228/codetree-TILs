# 원소의 수를 나타내는 n
n = int(input())

# n개의 원소가 공백을 사이에 두고 주어짐.
arr = list(map(int, input().split()))
idx = n - 1

while idx != 0 :
    # Algorithm
    # 1. 배열 전체를 순회하면서 가장 큰 수를 찾아서 반환하면서 인덱스를 저정한다.
    max_elem = -1
    for i in range(n) :
        if max_elem < arr[i] :
            max_elem = arr[i]
            idx = i
    # 최종, idx 에는 처음에 나온 가장 큰수의 index를 답고 있으면, 가장 큰 요소가 max_elem에 담아있게 됨.
    # 최댓값의 위치 출력
    print(idx+1, end = " ")
    # 2. 이 이후부터는 위에서 구한 최댓값의 idx 위치 왼쪽부분에만 탐색이 진행되어야함.
    #    arr에 idx 왼쪽 까지만을 다시 대입
    arr = arr[:idx]
    n = len(arr)