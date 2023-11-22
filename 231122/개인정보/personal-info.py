class Student :
    def __init__(self, name, height, weight) :
        self.name, self.height, self.weight = name, height, weight

n = 5
students = []
for _ in range(n) :
    n, h, w = tuple(input().split())
    students.append(Student(n, int(h), w))

students.sort(key= lambda x : x.name)
print("name")
for student in students :
    print(student.name, student.height, student.weight)

print()
students.sort(key= lambda x : -x.height)
print("height")
for student in students :
    print(student.name, student.height, student.weight)