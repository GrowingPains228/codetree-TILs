N, K = tuple(map(int, input().split()))

block_Arr = [0] + [0 for _ in range(N + 1)]

for _ in range(K) :
    A, B = tuple(map(int, input().split()))
    for i in range(A,B+1) :
        block_Arr[i] += 1
    
print(max(block_Arr))