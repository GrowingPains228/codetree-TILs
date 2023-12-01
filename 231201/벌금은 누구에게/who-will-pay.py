n, m, k = tuple(map(int, input().split()))
students = [0]*(n + 1)

student = -1
for _ in range(m) :
    idx = int(input())

    students[idx] += 1
    
    if students[idx] >= k and student == -1:
        student = idx

print(student)