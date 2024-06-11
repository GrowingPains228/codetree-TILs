n1, n2 = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s1 = set()
s2 = set()
for elem in A:
    s1.add(elem)

for eleme in B:
    s2.add(elem)

for elem in B:
    if elem in s1:
        s1.remove(elem)

for eleme in A:
    if elem in s2:
        s2.remove(elem)

print(len(s1) + len(s2))