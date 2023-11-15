char = input()

next_num = (ord(char)%(ord('z')+1) + 1)
print(chr(next_num))