class User :
    def __init__(self, name, address, local) :
        self.name = name
        self.address = address
        self.local = local

n = int(input())
people = []

for i in range(n) :
    name, address, local = tuple(input().split())
    people.append(User(name, address, local))

last_user = people[0]
for i in range(1,n) :
    if last_user.name < people[i].name :
        last_user = people[i]

# 사전순으로 가장 느린 사람 출력하기
print(f"name {last_user.name}")
print(f"addr {last_user.address}")
print(f"city {last_user.local}")