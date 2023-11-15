string = input()

sum_num = 0
# 해설이 제시하는 방법을 구현
for elem in string :
    if elem >= '0' and elem <= '9' :
        sum_num += int(elem)

print(sum_num)