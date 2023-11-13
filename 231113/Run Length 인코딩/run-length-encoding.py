A = input()
new_a = []

cnt = 1
temp_char = A[0]
index = 1
new_str = ""
while len(A) > index :
    if temp_char == A[index] :
        cnt += 1

    if temp_char != A[index] :
        temp_char = temp_char + str(cnt)
        new_str += temp_char
        temp_char = A[index]
        cnt = 1

    index += 1

temp_char = temp_char + str(cnt)
new_str += temp_char

print(len(new_str))
print(new_str)