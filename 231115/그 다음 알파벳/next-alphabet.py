char = input()

next_num = (ord(char)%ord('a')+ord('a')+1)
print(chr(next_num))