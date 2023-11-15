char = input()

next_num = 0

if ord(char)%ord('z') == 0 :
    next_num = ord('a')
else :
    next_num = ord(char)%ord('z') + 1

print(chr(next_num))