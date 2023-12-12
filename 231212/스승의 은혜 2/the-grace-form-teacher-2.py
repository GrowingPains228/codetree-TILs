n,b = tuple(map(int, input().split()))

presents = [
    int(input()) for _ in range(n)
]

presents.sort()

max_students = 0
for i in range(n) :
    cash = b
    students = 0
    for j in range(n) :
        if cash >= presents[j] or cash >= presents[j]//2 :
            cash -= (presents[j]//2) if j == i else presents[j]
            students += 1
        
    max_students = max(max_students, students)

print(max_students)