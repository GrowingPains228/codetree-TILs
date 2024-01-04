n = int(input())
arr = list(map(int, input().split()))

def sort_radix(arr) :
    # 원소 개수 구하기
    length = len(arr)
    # 원소의 최댓값 구하기
    max_num = max(arr)
    # 원소의 자릿수 구하기
    digit_cnt = 0
    while max_num > 0 :
        max_num //= 10
        digit_cnt += 1

    #자릿수 arr 만들기
    for i in range(1, digit_cnt + 1) :
        new_arr = [[] for _ in range(10)]
        for j in range(n) :
            # 해당 자리수가 있는지 부터 검사해서 없다면 0에 자동으로 추가하기
            if arr[j] < 1 * (10**(i-1)) :
                new_arr[0].append(arr[j])
                continue
            
            # 해당 자리수에 값이 있다면 대입
            digit = 0
            if i == 1 :
                digit = arr[j] % 10
            else :
                digit = arr[j] % (10**i) // (10**(i-1))

            new_arr[digit].append(arr[j])
        
        k = 0
        storage_arr = [0] * length
        for j in range(10) :
            for elem in new_arr[j] :
                storage_arr[k] = elem
                k += 1

        arr = storage_arr[::]
    
    return arr

arr = sort_radix(arr)

for elem in arr :
    print(elem, end = " ")