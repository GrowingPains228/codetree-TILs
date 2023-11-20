import sys

# 해설 2번째 방법 - count
ASCCI_NUM = 128

str1 = input()
str2 = input()

count = [
    0 for _ in range(ASCCI_NUM)
]

for char1 in str1 :
    count[ord(char1)] += 1

for char2 in str2 : 
    count[ord(char2)] -= 1

for elem in count :
    if elem != 0 :
        print("No")
        sys.exit(0)

print("Yes")