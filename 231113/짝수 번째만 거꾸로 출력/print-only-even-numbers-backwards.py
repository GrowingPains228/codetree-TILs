string = input()
new_string = ""

for i in range(len(string)) :
    if (i+1)%2 == 0 :
        new_string += string[i]

print(new_string[::-1])