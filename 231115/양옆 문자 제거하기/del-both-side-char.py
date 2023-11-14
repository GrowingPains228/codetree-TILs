string = input()

# 첫번째 방법 : slicing
#string = string[:1] + string[2:-2] + string[-1:]


# 두번째 방법 : pop
string = list(string)
string.pop(1)
string.pop(-2)
string = ''.join(string)
print(string)