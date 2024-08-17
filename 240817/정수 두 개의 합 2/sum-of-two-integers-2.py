def count_pairs_with_sum_less_than_k(arr, k):
    arr.sort()

    j = n
    ans = 0
    for i in range(1, n+1):
        while j >= 1 and arr[i] + arr[j] > k:
            j -= 1
        
        if j <= i:
            break;
        
        ans += j - i

    return ans

n, k = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]

result = count_pairs_with_sum_less_than_k(arr, k)
print(result)