class Student :
    def __init__(self, height, weight, number) :
        self.height, self.weight, self.number = height, weight, number
    

n = int(input())
arr = [
    tuple(map(int, input().split())) for _ in range(n)
]
students = [
    Student(w,h,i) for i, (w,h) in enumerate(arr, start = 1)
]

students.sort(key = lambda x : (x.height, -x.weight))

for student in students :
    print(student.height, student.weight, student.number)