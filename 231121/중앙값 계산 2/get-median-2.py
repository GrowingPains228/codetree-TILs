n = int(input())
arr = list(map(int, input().split()))

# 중간값 출력해주는 함수
def print_middle_result(arr, idx) :
    sorting_arr = sorted(arr)
    middle_idx = idx//2
    print(sorting_arr[middle_idx], end = " ")

for i in range(n) :
    if (i+1) % 2 == 1:
        print_middle_result(arr[:i+1],i)