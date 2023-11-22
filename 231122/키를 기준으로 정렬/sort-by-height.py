class user :
    def __init__(self, name, hight, weight) :
        self.name = name
        self.hight = hight
        self.weight = weight

n = int(input())
arr = [
    tuple(input().split()) for _ in range(n)
]

Users = [
    user(name, hight, weight) for name, hight, weight in arr
]

Users.sort(lambda x : x.hight)
for i in range(n) :
    print(Users[i].name, Users[i].hight, Users[i].weight)