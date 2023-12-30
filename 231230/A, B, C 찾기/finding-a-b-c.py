arr = list(map(int, input().split()))
arr.sort()

# A,B 값이 제일 작게 나올것이고, A+B+C 값이 제일 크게 나올것이다.
A = arr[0]
B = arr[1]
C = arr[-1] - A - B
print(A, B, C)