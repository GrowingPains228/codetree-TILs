n = int(input())

strings_arr = []
for _ in range(n) :
    strings_arr.append(input())

strings_arr.sort()

for elem in strings_arr :
    print(elem)