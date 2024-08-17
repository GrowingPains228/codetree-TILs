def count_pairs_with_sum_less_than_k(arr, k):
    arr.sort()
    left, right = 0, len(arr) - 1
    count = 0
    
    while left < right:
        if arr[left] + arr[right] <= k:
            count += (right - left)
            left += 1
        else :
            right -= 1
    
    return count


n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

result = count_pairs_with_sum_less_than_k(arr, k)
print(result)