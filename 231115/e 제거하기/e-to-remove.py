string = input()
string = list(string)
string.pop(string.index('e'))
print(''.join(string))