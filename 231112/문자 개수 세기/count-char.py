string = input()
char = input()

cnt = 0
for i in range(len(string)) :
    if string[i] == char :
        cnt += 1
print(cnt)