n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
sum_arr1 = [0] * n
sum_arr2 = [0] * n
sum_arr1[0] = arr[0]
for i in range(1,n):
    sum_arr1[i] = sum_arr1[i-1] + arr[i]

sum_arr2[k-1] = sum_arr1[k-1]

for i in range(k, n):
    sum_arr2[i] = sum_arr1[i] - sum_arr1[i-k]

print(max(sum_arr2))