string = input()
L = len(string)

print(string)
# 오른쪽으로 한글자씩 밀어서 출력
for _ in range(L) :
    string = string[-1] + string[:-1]
    print(string)