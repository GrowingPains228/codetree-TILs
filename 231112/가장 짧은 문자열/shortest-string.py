str1 = input()
str2= input()
str3 = input()

str1_len = len(str1)
str2_len = len(str2)
str3_len = len(str3)

arr = [str1_len, str2_len, str3_len]

max_len = max(arr)
min_len = min(arr)

print(max_len - min_len)