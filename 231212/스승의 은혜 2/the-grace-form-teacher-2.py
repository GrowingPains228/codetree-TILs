n,b = tuple(map(int, input().split()))

presents = [
    int(input()) for _ in range(n)
]

presents.sort()

max_students = 0
for i in range(n) :
    cash = b
    students = 0
    presents[i] //= 2
    for j in range(n) :
        if cash >= presents[j] :
            cash -= presents[j]
            students += 1
        
    max_students = max(max_students, students)
    presents[i] *= 2

print(max_students)