class subject :
    def __init__ (self, name, kor, eng, math) :
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
students = []
for _ in range(n) :
    name, k, e, m = tuple(input().split())
    _ , k, e, m = ( _, int(k), int(e), int(m))
    students.append(subject(name, k, e, m))

students.sort(key = lambda x: (-x.kor, -x.eng, -x.math))

for elem in students :
    print(elem.name, elem.kor, elem.eng, elem.math)