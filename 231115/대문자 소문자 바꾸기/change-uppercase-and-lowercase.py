string = input()
temp_str = ""
for elem in string :
    if elem >= 'A' and elem <= 'Z' :
        temp_str += elem.lower()
    else :
        temp_str += elem.upper()
print(temp_str)