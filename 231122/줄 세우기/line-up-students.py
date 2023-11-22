class Student : 
    def __init__(self, height, weight, number) :
        self.height = height
        self.weight = weight
        self.number = number

n=  int(input())
students = []
for i in range(1,n + 1) :
    h,w = tuple(map(int, input().split()))
    students.append(Student(h,w,i))


students.sort(key = lambda x : (-x.height, -x.weight, x.number))

for student in students :
    print(student.height, student.weight, student.number)