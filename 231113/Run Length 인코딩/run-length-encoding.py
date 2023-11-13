A = input()
new_a = []

cnt = 1
temp_char = A[0]
index = 1
new_a.append(A[0])

while len(A) > index :
    if temp_char == A[index] :
        cnt += 1

    if temp_char != A[index] :
        new_a.append(cnt)
        temp_char = A[index]
        new_a.append(temp_char)
        cnt = 1

    index += 1

new_a.append(cnt)


print(len(new_a))
for elem in new_a :
    print(elem, end="")