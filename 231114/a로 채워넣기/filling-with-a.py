string = list(input())

string[1] = string[-2] = 'a'
string = ''.join(string)

print(string)