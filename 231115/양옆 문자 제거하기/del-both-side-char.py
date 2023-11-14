string = input()

# 첫번째 방법 : slicing
string = string[:1] + string[2:-2] + string[-1:]
print(string) #