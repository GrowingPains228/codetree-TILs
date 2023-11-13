n = 10
string_arr = [
    input() for _ in range(n)
]
end_char = input()

existence = False
for elem in string_arr :
    if elem[-1] == end_char :
        print(elem)
        existence = True

if existence is not True :
    print("None")