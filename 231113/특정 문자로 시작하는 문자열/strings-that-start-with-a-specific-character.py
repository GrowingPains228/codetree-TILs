n = int(input())

string_arr = [
    input() for _ in range(n)
]

a = input()
cnt = 0
len_num = 0

for elem in string_arr :
    if elem[0] == a :
        cnt += 1
        len_num += len(elem)

print(cnt, f"{(len_num/cnt):.2f}")