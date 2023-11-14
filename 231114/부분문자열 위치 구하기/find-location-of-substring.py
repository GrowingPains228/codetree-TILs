string = input()
goal_string = input()

#1. 쉬운 방법 (find keyword로 바로 해결)
#print(string.find(goal_string))

#2.  for loop 돌면서 비교하기
leng = len(string)
leng_goal = len(goal_string)
index = -1

for i in range(leng -leng_goal + 1) :
    if goal_string == string[i:i + leng_goal] :
        index = i
        break

print(index)