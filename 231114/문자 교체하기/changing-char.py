string1, string2 = tuple(map(list,input().split()))

string2[:2] = string1[:2]
print(''.join(string2))