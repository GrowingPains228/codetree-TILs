char1= input()
char2= input()

char1 = sorted(char1)
char2 = sorted(char2)

isSame = True
for c1,c2 in zip(char1, char2) :
    if c1 != c2 :
        isSame = False
        break

print("Yes" if isSame else "No")