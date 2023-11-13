in_ee = "ee"
in_ab = "ab"

arr = input()

# 1. 가장 쉬운 in 키워드를 써서 비교하는 방법
#if in_ee in arr :
#    print("Yes", end = " ")
#else :
#    print("No")

#if in_ab in arr :
#    print("Yes", end = " ")
#else :
#    print("No")

#2. 길이만큼 전부 비교하기
len_ee = len("ee")
len_ab = len("ab")

exits_tf = False
for i in range(len(arr) -1) :
    if in_ee == arr[i:i+len_ee] :
        exits_tf = True
        break
    
print("Yes" if exits_tf else "No", end = " ")

exits_tf = False
for i in range(len(arr) -1) :
    if in_ab == arr[i:i+len_ab] :
        exits_tf = True
        break
    
print("Yes" if exits_tf else "No")