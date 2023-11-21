class User :
    def __init__(self, name, address, local) :
        self.name = name
        self.address = address
        self.local = local

n = int(input())
people = []
for _ in range(n) :
    name, address, local = tuple(input().split())
    people.append(User(name, address, local))

print(f"name {people[n-1].name}")
print(f"addr {people[n-1].address}")
print(f"city {people[n-1].local}")