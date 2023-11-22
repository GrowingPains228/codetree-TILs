class Student : 
    def __init__(self, name, height, weight) :
        self.name, self.height, self.weight = name, height, weight


n = int(input())
students = []
for _ in range(n) :
    n, h, w = tuple(input().split())
    students.append(Student(n, int(h), int(w)))

students.sort(key=lambda x : (x.height, -x.weight))
for student in students :
    print(student.name, student.height, student.weight)