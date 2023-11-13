n = int(input())
string_arr = []
sum_len = 0
a_cnt = 0

for _ in range(n) :
    string = input()
    sum_len += len(string)
    if string[0] == 'a' :
        a_cnt += 1
    string_arr.append(string)

print(sum_len, a_cnt)