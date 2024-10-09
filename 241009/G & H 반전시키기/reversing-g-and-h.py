n = int(input())
string = input()
goalstring = input()

ansList = 0 

startIdx = 0
endIdx = 0
countOn = False
for i in range(n):
    if string[i] == goalstring[i]:
        if countOn:
            ansList += 1
            countOn = False
        continue

    if i == n-1 and string[i] != goalstring[i] :
        ansList += 1
        break
    
    countOn = True

print(ansList)