n, m, k = tuple(map(int, input().split()))
students = [0]*(n + 1)

for _ in range(m) :
    idx = int(input())
    students[idx] += 1

student = -1
for i in range(1, n + 1) :
    if students[i] >= k :
        student = i
        break
print(student)