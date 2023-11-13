arr = ["apple", "banana", "grape", "blueberry", "orange"]
char = input()
cnt = 0

for string_elem in arr :
    if char not in string_elem :
        continue
    
    # 이렇게 하면 해당 char 가 여러개 있다면, 제일 처음에 찾아지는 문자의 index 만 나옴.
    #if string_elem.index(char) in (2,3) :
    #    print(string_elem)
    #    cnt += 1

    if string_elem[2] == char or string_elem[3] == char :
        print(string_elem)
        cnt += 1
print(cnt)