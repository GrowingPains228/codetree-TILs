string1 = input()
string2 = input()

remove_alpha1 = ""
remove_alpha2 = ""

for elem in string1 :
    if elem.isdigit() :
        remove_alpha1 += elem
    
for elem in string2 :
    if elem.isdigit() :
        remove_alpha2 += elem

print(int(remove_alpha1) + int(remove_alpha2))