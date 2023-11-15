string_arr = []

while True :
    string = input()

    if string == '0' :
        break

    string_arr.append(string)
    
print(len(string_arr))
for i in range(len(string_arr)) :
    if (i+1)%2 == 1 :
        print(string_arr[i])